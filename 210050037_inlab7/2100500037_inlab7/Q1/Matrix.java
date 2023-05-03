package Q1;

public class Matrix {
    private int n,m ;
    private int mat[][] ;

    Matrix(int n, int m, int v) {
        /* 
         * TODO: Complete this constructor
         * Initialize a matrix of size n x m with all elements equal to v
         */
         this.n=n;this.m=m;
         mat=new int[n][m];
         for(int i=0;i<n;i++){
         	for(int j=0;j<m;j++){
         		mat[i][j]=v;
         		}
         	}
    }

    Matrix(int n, int m) {
        /* 
         * TODO: Complete this constructor 
         * Initialize a matrix of size n x m with all elements equal to 0
         */
         this.m=m;this.n=n;
         mat=new int[n][m];
         for(int i=0;i<n;i++){
         	for(int j=0;j<m;j++){
         		mat[i][j]=0;
         		}
         	}
    }

    static Matrix add(Matrix A, Matrix B) {
        /*
         * TODO: Complete this method
         * Add two matrices and return the result
         */
         if(A.n!=B.n || A.m!=B.m){
         Matrix z = new Matrix(1,1);
         return z;
         }
         int n=A.n;
         int m=A.m;
        Matrix C = new Matrix(n,m);
        for(int i=0;i<n;i++){
         	for(int j=0;j<m;j++){
         		C.mat[i][j]=A.mat[i][j]+B.mat[i][j];
         		}
         	}
         return C;
    
    }

    static Matrix matmul(Matrix A, Matrix B) {
        /*
         * TODO: Complete this method
         * Multiply two matrices and return the result
         * and return a zero matrix of size 1 x 1
         */
         if(A.m!=B.n){
         Matrix z = new Matrix(1,1);
         return z;}
         int n=A.n;int m=B.m;int k=A.m;
         Matrix C = new Matrix(n,m);
         for(int i=0;i<n;i++){
         	for(int j=0;j<m;j++){
         		for(int r=0;r<k;r++){
         		C.mat[i][j]=C.mat[i][j]+A.mat[i][r]*B.mat[r][j];
         		}
         	}
         }
         return C;
    }

    void scalarmul(int k) {
        /*
         * TODO: Complete this method
         * Multiply all elements of the matrix by k
         */
         for(int i=0;i<n;i++){
         	for(int j=0;j<m;j++){
         		mat[i][j]=k*mat[i][j];
         		}
         	}
         return;
    }

    int getrows() {
        /*
         * TODO: Complete this method
         * Return the number of rows in the matrix
         */
         return n;
    }

    int getcols() {
        /*
         * TODO: Complete this method
         * Return the number of columns in the matrix
         */
         return m;
    }

    int getelem(int i,int j) {
        /*
         * TODO: Complete this method
         * Return the element at row i and column j
         * If i or j is out of bounds, return -1
         */
         if(i>=n || j>=m || i<0 || j<0){
         return -1;
         }
         return mat[i][j];
    }

    void setelem(int i,int j, int v) {
        /*
         * TODO: Complete this method
         * Set the element at row i and column j to v
         * If i or j is out of bounds, don't change anything
         */
         if(i>=n || j>=m || i<0 || j<0){
         return;
         }
         mat[i][j]=v;
         return;
    }

    void printmatrix() {
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(j!=0) System.out.print(" ");
                System.out.print(mat[i][j]);
            }
            System.out.print("\n") ;
        }
    }
}

