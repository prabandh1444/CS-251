package Q2 ;

public class Board {
    private int [][] board = new int[3][3];
    /* elements of board is either 0, 1 or 2 
     * 0 means empty
     * 1 means player 1's token  (say X)
     * 2 means player 2's token  (say O)
     */

    public void printBoard(){
        /*
         * Don't change this function
         */
        System.out.println("Board:");
        System.out.println("-------------");
        for(int i=0;i<3;i++){
            System.out.print("| ");
            for(int j=0;j<3;j++){
                if(board[i][j]==0){
                    System.out.print(" ");
                }
                else if(board[i][j]==1){
                    System.out.print("X");
                }
                else if(board[i][j]==2){
                    System.out.print("O");
                }
                System.out.print(" | ");
            }
            System.out.println("\n-------------");   
        }
    }

    public Boolean available(Integer x, Integer y){
        /*
         * TODO: Check if the position (x,y) is available
         * return true if available. 
         * Also return false if (x,y) is not a valid position
         */
        if(x<0 || x>3 || y<0 || y>3) return false;
        else if(board[x][y]==0) return true;
        else return false;

    }


    public void updateBoard(Integer[] pos, Integer id){
        /*
         * TODO: Update the board 
         */
        board[pos[0]][pos[1]] = id;
        return;
    }

    // create any helper functions you need

    

    public int checkBoard() {
        printBoard();
        /*
         * Don't remove the above line
         */

        // EDIT BELOW THIS LINE
        /*
         * TODO: Check the board and return the status of the game
         * -1 if Game has Not yet Ended
         * 0 if Game has Ended in a Draw
         * 1 if Player 1 has Won
         * 2 if Player 2 has Won
         */
        int empty=0;
        for (int a = 0; a < 8; a++) {
            String line = null;
  
            switch (a) {
            case 0:
                line = Integer.toString(board[0][0]) + Integer.toString(board[0][1]) + Integer.toString(board[0][2]);
                break;
            case 1:
                line = Integer.toString(board[1][0]) + Integer.toString(board[1][1]) + Integer.toString(board[1][2]);
                break;
            case 2:
                line = Integer.toString(board[2][0]) + Integer.toString(board[2][1]) + Integer.toString(board[2][2]);
                break;
            case 3:
                line = Integer.toString(board[0][0]) + Integer.toString(board[1][0]) + Integer.toString(board[2][0]);
                break;
            case 4:
                line = Integer.toString(board[0][1]) + Integer.toString(board[1][1]) + Integer.toString(board[2][1]);
                break;
            case 5:
                line = Integer.toString(board[0][2]) + Integer.toString(board[1][2]) + Integer.toString(board[2][2]);
                break;
            case 6:
                line = Integer.toString(board[0][0]) + Integer.toString(board[1][1]) + Integer.toString(board[2][2]);
                break;
            case 7:
                line = Integer.toString(board[0][2]) + Integer.toString(board[1][1]) + Integer.toString(board[2][0]);
                break;
            }
            //For X winner
            if (line.equals("111")) {
                return 1;
            }
              
            // For O winner
            else if (line.equals("222")) {
                return 2;
            }
            else if(line.charAt(0)=='0'||line.charAt(1)=='0'||line.charAt(2)=='0'){
                empty++;
            }
        }
         if(empty==0){return 0;}
         else return -1;
        
    }
}
