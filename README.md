
# Chess Game Using Image Processing

## Overview
This project builds a dynamic chessboard game using image processing techniques. The application detects chessboard lines, identifies squares, and places chess pieces on the board. Additionally, it applies transformations to create a 3D effect on the board.

The project is implemented in Python using the **OpenCV** library for image processing and consists of the following parts:
1. **Line Detection**: Detect lines on the chessboard using Hough Transforms.
2. **Square Detection**: Count the number of squares on the board using contours.
3. **Piece Placement**: Place chess pieces on the board dynamically.
4. **3D Transformations**: Apply transformations to give the chessboard a realistic 3D appearance.

---

## File Structure

### `utils.py`
Contains helper functions for the following tasks:
- **Line Detection**: `apply_hough_lines` detects lines using Hough Transform.
- **Square Detection**: `process_contours` identifies square areas on the chessboard.
- **Piece Placement**: `place_pieces` maps and places chess pieces onto the board based on a given mapping.
- **Transformations**:
  - `apply_perspective_transformation`: Adds depth to the board using perspective transformation.
  - `apply_affine_transformation`: Skews the board to enhance 3D effects.
  - `apply_rotation`: Rotates the board for dynamic visualization.
  - `apply_transformations`: Combines all transformations.

### `main.py`
The main script that integrates all functionalities:
1. Loads the chessboard and piece images.
2. Detects lines and squares on the board.
3. Places chess pieces on the detected squares based on a mapping.
4. Applies 3D transformations to the chessboard for visual enhancement.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Chess-Game-Using-Image-Processing
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python numpy
   ```
3. Ensure the following folder structure for images and set correct path in the main.py file:
   ```
   Images of Chess board/
       chess.png
       white_pawn.png
       white_rook.png
       white_knight.png
       white_bishop.png
       white_queen.png
       white_king.png
       black_pawn.png
       black_rook.png
       black_knight.png
       black_bishop.png
       black_queen.png
       black_king.png
   ```

---

## Usage

1. Set paths to the chessboard and chess piece images in `main.py`.
2. Run the script:
   ```bash
   python main.py
   ```
3. The program will:
   - Detect lines and squares on the chessboard.
   - Place the chess pieces on the board.
   - Apply transformations to display a 3D chessboard.

---

## Functions in `utils.py`

### Part 1: Line Detection
- **`apply_hough_lines`**:
  Detects lines on the board using Hough Line Transform and highlights them.

### Part 2: Square Detection
- **`process_contours`**:
  Identifies squares based on contour area and approximates their corners.

### Part 3: Piece Placement
- **`place_pieces`**:
  Dynamically places chess pieces on the board using perspective transformations.

### Part 4: Transformations
- **`apply_perspective_transformation`**:
  Adds a 3D effect by applying perspective transformation.
- **`apply_affine_transformation`**:
  Skews the board using affine transformation.
- **`apply_rotation`**:
  Rotates the chessboard for a dynamic view.
- **`apply_transformations`**:
  Combines all transformations for a complete visual enhancement.

---

## Outputs

- **Final Chessboard**: A transformed board with lines, squares, and chess pieces placed accurately.
- **Statistics**: Displays the total number of detected squares.

---

## Requirements

- Python 3.7+
- OpenCV
- NumPy

---

## Future Enhancements

- Implement interactive gameplay for chess.
- Integrate move validation and piece tracking.
- Support for custom chessboard images and piece sets.

