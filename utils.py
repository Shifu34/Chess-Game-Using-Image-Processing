import pandas as pd
import cv2
import numpy as np
"""part 4 helper functions"""
def apply_perspective_transformation(board_image):
    h, w = board_image.shape[:2]
    src_points = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
    dst_points = np.float32([[w*0.2, h*0.2], [w*0.8, h*0.2], [w*0.8, h*0.8], [w*0.2, h*0.8]])
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    transformed_board = cv2.warpPerspective(board_image, matrix, (w, h))
    return transformed_board

def apply_affine_transformation(board_image):
    h, w = board_image.shape[:2]
    src_points = np.float32([[0, 0], [w, 0], [0, h]])
    dst_points = np.float32([[w*0.3, h*0.2], [w*0.7, h*0.3], [w*0.2, h*0.8]])
    matrix = cv2.getAffineTransform(src_points, dst_points)
    transformed_board = cv2.warpAffine(board_image, matrix, (w, h))
    return transformed_board

def apply_rotation(board_image, angle):
    (h, w) = board_image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_board = cv2.warpAffine(board_image, matrix, (w, h))
    return rotated_board

def apply_transformations(board_image):
    # Applying perspective transformation
    perspective_board = apply_perspective_transformation(board_image)
    # Applying affine transformation for a skew effect
    affine_board = apply_affine_transformation(perspective_board)
    # Applying rotation for dynamic effect
    rotated_board = apply_rotation(affine_board, angle=20)
    return rotated_board
"""part 1 helper function"""
def apply_hough_lines(board_image):
    edges = cv2.Canny(board_image, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(board_image, (x1, y1), (x2, y2), (0, 255, 0), 2) 
    return board_image
"""part 2 helper function"""
def process_contours(board_contours, original_image):
    square_centers = []  
    board_squared = original_image.copy()  
    for contour in board_contours:
        contour_area = cv2.contourArea(contour)
        if 1000 < contour_area < 20000:
            epsilon = 0.05 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            if len(approx) == 4:
                pts = [pt[0] for pt in approx]  # Extract the coordinates
                pt1, pt2, pt3, pt4 = tuple(pts[0]), tuple(pts[1]), tuple(pts[2]), tuple(pts[3])
                x, y, w, h = cv2.boundingRect(contour)
                center_x = int(x + w / 2)
                center_y = int(y + h / 2)
                square_centers.append([center_x, center_y, pt1, pt2, pt3, pt4])

                cv2.line(board_squared, pt1, pt2, (255, 255, 0), 7)
                cv2.line(board_squared, pt2, pt4, (255, 255, 0), 7)
                cv2.line(board_squared, pt4, pt3, (255, 255, 0), 7)
                cv2.line(board_squared, pt3, pt1, (255, 255, 0), 7)
    return square_centers, board_squared
"""part 3 helper function"""
def place_pieces(board_image, square_centers, piece_mapping, piece_images):
    for idx, (center_x, center_y, pt1, pt2, pt3, pt4) in enumerate(square_centers):
        # Checking if there is a piece to be placed in this square
        if idx + 1 in piece_mapping:
            piece_name = piece_mapping[idx + 1]
            piece_img = piece_images[piece_name]
            # Calculating the size of the square
            x1, y1 = pt1
            x2, y2 = pt2
            side_length = int(np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
            # Resizing the piece image to fit the square
            piece_resized = cv2.resize(piece_img, (side_length, side_length))
            h, w = piece_resized.shape[:2]

            src_p = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
            dst_p = np.float32([pt1, pt2, pt3, pt4])

            matrix = cv2.getPerspectiveTransform(src_p, dst_p)
            warped_piece = cv2.warpPerspective(piece_resized, matrix, (board_image.shape[1], board_image.shape[0]))

            # Creating a mask for the piece image (to blend it with the board)
            piece_mask = np.zeros((board_image.shape[0], board_image.shape[1]), dtype=np.uint8)
            warped_piece_gray = cv2.cvtColor(warped_piece, cv2.COLOR_BGR2GRAY)
            _, piece_mask = cv2.threshold(warped_piece_gray, 1, 255, cv2.THRESH_BINARY)
            piece_mask_inv = cv2.bitwise_not(piece_mask)
            # Masking out the area on the board where the piece will go
            board_background = cv2.bitwise_and(board_image, board_image, mask=piece_mask_inv)
            # Using the mask to extract the warped piece
            piece_foreground = cv2.bitwise_and(warped_piece, warped_piece, mask=piece_mask)
            # Adding the piece to the board
            board_image = cv2.add(board_background, piece_foreground)
    return board_image
"""Main Function """
def Chess_Game(img_path, piece_mapping, piece_images):
    chess = cv2.imread(img_path)
    gray_image = cv2.cvtColor(chess, cv2.COLOR_BGR2GRAY)
    gaussian_blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
    _, otsu_binary = cv2.threshold(gaussian_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Applying Hough Line Transform before contour processing
    board_with_lines = apply_hough_lines(otsu_binary)
    edges = cv2.Canny(board_with_lines, 50, 150, apertureSize=3)
    kernel = np.ones((7, 7), np.uint8)
    img_dilation = cv2.dilate(edges, kernel, iterations=1)
    kernel = np.ones((3, 3), np.uint8)
    img_dilation_2 = cv2.dilate(img_dilation, kernel, iterations=1)
    board_contours, _ = cv2.findContours(img_dilation_2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Processing contours after applying Hough Line Transform
    square_centers, board_with_rectangles = process_contours(board_contours, chess)
    # Placing both white and black pieces on the board
    board_with_pieces = place_pieces(board_with_rectangles, square_centers, piece_mapping, piece_images)
    transformed_board = apply_transformations(board_with_pieces)
    # Showing the final board with placed pieces and detected lines
    cv2.imshow("Board with Pieces and Lines", transformed_board)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(f"Total Number of Squares: {len(square_centers)}")