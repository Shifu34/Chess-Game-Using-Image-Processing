from utils import *

"""
In this task I will be building a chess game using Image Processing.
This task is divided into four parts. 

Part 1:
     In this part I am detecting lines on chess board using hough transforms.

Part 2: 
    In this part I am counting the number of boxes on the chessboard. This is done by this custom made function process_contours(). 
    This function is used to detect the boxes on the chessboard with the help of cv2.contourArea. If the area is in the 
    range of 2000 to 20000 then it is a box in the chessboard. Then it approximate the box points using cv2.approxPolyDP().
    After this it store the centers and corners of the boxes in a list so that it can be used for further processing.

Part 3:
    In this part I am placing the chess pieces on the chess board. For this purpose I have made a custom function place_pieces().
    This function is taking the mapping of the pieces along with the images of the pieces. The mapping is done like the standard 
    chessboard. Firstly, it take the image name and the mapping place and then reshaping the piece image to the box size. After this,
    it uses cv2.getPerspectiveTransform() to get a transformation matrix which is then used in this cv2.warpPerspective() to get a 
    wraped image. Then it creates a mask so that it can blend the piece image with the chessboard. It also mask out the area on
    the board where the piece will go and use the mask to extract the warped piece. In the end it add the piece on the board.

Part 4:
    In this part I am give the chessboard a 3d look. For this I have created four helper functions in which I am applying perspective
    transformation, affine transformation and rotating the board. Perspective Transformtion is used to create a 3d effect and then affine
    transformation is used to create skewness in the board, and in the end rotating the board for a better and a 3d look.
"""

if __name__ == "__main__":
    # Paths to images
    chess_board = "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\chess.png"
    piece_images_paths = {
        'white_pawn': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\white_pawn.png",
        'white_rook': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\white_rook.png",
        'white_knight': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\white_knight.png",
        'white_bishop': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\white_bishop.png",
        'white_queen': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\white_queen.png",
        'white_king': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\white_king.png",
        'black_pawn': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\\black_pawn.png",
        'black_rook': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\\black_rook.png",
        'black_knight': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\\black_knight.png",
        'black_bishop': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\\black_bishop.png",
        'black_queen': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\\black_queen.png",
        'black_king': "C:\Users\shafq\Desktop\Chess-Game-Using-Image-Processing\Images of Chess board\\black_king.png"
    }
    piece_mapping = {
        # White pieces in squares 1-16
        1: 'white_rook', 2: 'white_knight', 3: 'white_bishop', 4: 'white_king', 5: 'white_queen', 
        6: 'white_bishop', 7: 'white_knight', 8: 'white_rook',
        9: 'white_pawn', 10: 'white_pawn', 11: 'white_pawn', 12: 'white_pawn', 
        13: 'white_pawn', 14: 'white_pawn', 15: 'white_pawn', 16: 'white_pawn',

        # Black pieces in squares 49-64
        57: 'black_rook', 58: 'black_knight', 59: 'black_bishop', 60: 'black_king', 61: 'black_queen', 
        62: 'black_bishop', 63: 'black_knight', 64: 'black_rook',
        49: 'black_pawn', 50: 'black_pawn', 51: 'black_pawn', 52: 'black_pawn', 
        53: 'black_pawn', 54: 'black_pawn', 55: 'black_pawn', 56: 'black_pawn'
    }

    piece_images = {
        'white_pawn': cv2.imread(piece_images_paths['white_pawn']),
        'white_rook': cv2.imread(piece_images_paths['white_rook']),
        'white_knight': cv2.imread(piece_images_paths['white_knight']),
        'white_bishop': cv2.imread(piece_images_paths['white_bishop']),
        'white_queen': cv2.imread(piece_images_paths['white_queen']),
        'white_king': cv2.imread(piece_images_paths['white_king']),
        'black_pawn': cv2.imread(piece_images_paths['black_pawn']),
        'black_rook': cv2.imread(piece_images_paths['black_rook']),
        'black_knight': cv2.imread(piece_images_paths['black_knight']),
        'black_bishop': cv2.imread(piece_images_paths['black_bishop']),
        'black_queen': cv2.imread(piece_images_paths['black_queen']),
        'black_king': cv2.imread(piece_images_paths['black_king'])
    }

    Chess_Game(chess_board, piece_mapping, piece_images)