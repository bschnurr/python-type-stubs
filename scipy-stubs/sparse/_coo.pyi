"""
This type stub file was generated by pyright.
"""

from ._data import _data_matrix, _minmax_mixin
from ._csc import csc_matrix
from ._csr import csr_matrix
from ._dia import dia_matrix
from ._dok import dok_matrix

from numpy.typing import NDArray
from numpy import float64

""" A sparse matrix in COOrdinate or 'triplet' format"""
__docformat__ = ...
__all__ = ['coo_matrix', 'isspmatrix_coo']
class coo_matrix(_data_matrix, _minmax_mixin):
    """
    A sparse matrix in COOrdinate format.

    Also known as the 'ijv' or 'triplet' format.

    This can be instantiated in several ways:
        coo_matrix(D)
            with a dense matrix D

        coo_matrix(S)
            with another sparse matrix S (equivalent to S.tocoo())

        coo_matrix((M, N), [dtype])
            to construct an empty matrix with shape (M, N)
            dtype is optional, defaulting to dtype='d'.

        coo_matrix((data, (i, j)), [shape=(M, N)])
            to construct from three arrays:
                1. data[:]   the entries of the matrix, in any order
                2. i[:]      the row indices of the matrix entries
                3. j[:]      the column indices of the matrix entries

            Where ``A[i[k], j[k]] = data[k]``.  When shape is not
            specified, it is inferred from the index arrays

    Attributes
    ----------
    dtype : dtype
        Data type of the matrix
    shape : 2-tuple
        Shape of the matrix
    ndim : int
        Number of dimensions (this is always 2)
    nnz
        Number of stored values, including explicit zeros
    data
        COO format data array of the matrix
    row
        COO format row index array of the matrix
    col
        COO format column index array of the matrix

    Notes
    -----

    Sparse matrices can be used in arithmetic operations: they support
    addition, subtraction, multiplication, division, and matrix power.

    Advantages of the COO format
        - facilitates fast conversion among sparse formats
        - permits duplicate entries (see example)
        - very fast conversion to and from CSR/CSC formats

    Disadvantages of the COO format
        - does not directly support:
            + arithmetic operations
            + slicing

    Intended Usage
        - COO is a fast format for constructing sparse matrices
        - Once a matrix has been constructed, convert to CSR or
          CSC format for fast arithmetic and matrix vector operations
        - By default when converting to CSR or CSC format, duplicate (i,j)
          entries will be summed together.  This facilitates efficient
          construction of finite element matrices and the like. (see example)

    Examples
    --------

    >>> # Constructing an empty matrix
    >>> from scipy.sparse import coo_matrix
    >>> coo_matrix((3, 4), dtype=np.int8).toarray()
    array([[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]], dtype=int8)

    >>> # Constructing a matrix using ijv format
    >>> row  = np.array([0, 3, 1, 0])
    >>> col  = np.array([0, 3, 1, 2])
    >>> data = np.array([4, 5, 7, 9])
    >>> coo_matrix((data, (row, col)), shape=(4, 4)).toarray()
    array([[4, 0, 9, 0],
           [0, 7, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 5]])

    >>> # Constructing a matrix with duplicate indices
    >>> row  = np.array([0, 0, 1, 3, 1, 0, 0])
    >>> col  = np.array([0, 2, 1, 3, 1, 0, 0])
    >>> data = np.array([1, 1, 1, 1, 1, 1, 1])
    >>> coo = coo_matrix((data, (row, col)), shape=(4, 4))
    >>> # Duplicate indices are maintained until implicitly or explicitly summed
    >>> np.max(coo.data)
    1
    >>> coo.toarray()
    array([[3, 0, 1, 0],
           [0, 2, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 1]])

    """
    format = ...
    def __init__(self, arg1, shape=..., dtype=..., copy=...) -> None:
        ...
    
    def reshape(self, *args, **kwargs) -> "coo_matrix":
        ...
    
    def getnnz(self, axis=...): # -> int | NDArray[intp]:
        ...
    
    def transpose(self, axes=..., copy=...)-> "coo_matrix":
        ...
    
    def resize(self, *shape) -> None:
        ...
    
    def toarray(self, order=..., out=...) -> NDArray[float64]:
        """See the docstring for `spmatrix.toarray`."""
        ...
    
    def tocsc(self, copy=...) -> csc_matrix:
        """Convert this matrix to Compressed Sparse Column format

        Duplicate entries will be summed together.

        Examples
        --------
        >>> from numpy import array
        >>> from scipy.sparse import coo_matrix
        >>> row  = array([0, 0, 1, 3, 1, 0, 0])
        >>> col  = array([0, 2, 1, 3, 1, 0, 0])
        >>> data = array([1, 1, 1, 1, 1, 1, 1])
        >>> A = coo_matrix((data, (row, col)), shape=(4, 4)).tocsc()
        >>> A.toarray()
        array([[3, 0, 1, 0],
               [0, 2, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 1]])

        """
        ...
    
    def tocsr(self, copy=...) -> csr_matrix:
        """Convert this matrix to Compressed Sparse Row format

        Duplicate entries will be summed together.

        Examples
        --------
        >>> from numpy import array
        >>> from scipy.sparse import coo_matrix
        >>> row  = array([0, 0, 1, 3, 1, 0, 0])
        >>> col  = array([0, 2, 1, 3, 1, 0, 0])
        >>> data = array([1, 1, 1, 1, 1, 1, 1])
        >>> A = coo_matrix((data, (row, col)), shape=(4, 4)).tocsr()
        >>> A.toarray()
        array([[3, 0, 1, 0],
               [0, 2, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 1]])

        """
        ...
    
    def tocoo(self, copy=...) -> "coo_matrix":
        ...
    
    def todia(self, copy=...) -> dia_matrix:
        ...
    
    def todok(self, copy=...) -> dok_matrix:
        ...
    
    def diagonal(self, k=...) -> NDArray[float64]:
        ...
    
    def sum_duplicates(self): # -> None:
        """Eliminate duplicate matrix entries by adding them together

        This is an *in place* operation
        """
        ...
    
    def eliminate_zeros(self) -> None:
        """Remove zero entries from the matrix

        This is an *in place* operation
        """
        ...
    


def isspmatrix_coo(x) -> bool:
    """Is x of coo_matrix type?

    Parameters
    ----------
    x
        object to check for being a coo matrix

    Returns
    -------
    bool
        True if x is a coo matrix, False otherwise

    Examples
    --------
    >>> from scipy.sparse import coo_matrix, isspmatrix_coo
    >>> isspmatrix_coo(coo_matrix([[5]]))
    True

    >>> from scipy.sparse import coo_matrix, csr_matrix, isspmatrix_coo
    >>> isspmatrix_coo(csr_matrix([[5]]))
    False
    """
    ...

