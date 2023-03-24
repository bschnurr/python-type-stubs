"""
This type stub file was generated by pyright.
"""

from typing import Generator
from ._compressed import _cs_matrix
from ._csc import csc_matrix
from ._lil import lil_matrix
from ._bsr import bsr_matrix

"""Compressed Sparse Row matrix format"""
__docformat__ = ...
__all__ = ['csr_matrix', 'isspmatrix_csr']
class csr_matrix(_cs_matrix):
    """
    Compressed Sparse Row matrix

    This can be instantiated in several ways:
        csr_matrix(D)
            with a dense matrix or rank-2 ndarray D

        csr_matrix(S)
            with another sparse matrix S (equivalent to S.tocsr())

        csr_matrix((M, N), [dtype])
            to construct an empty matrix with shape (M, N)
            dtype is optional, defaulting to dtype='d'.

        csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
            where ``data``, ``row_ind`` and ``col_ind`` satisfy the
            relationship ``a[row_ind[k], col_ind[k]] = data[k]``.

        csr_matrix((data, indices, indptr), [shape=(M, N)])
            is the standard CSR representation where the column indices for
            row i are stored in ``indices[indptr[i]:indptr[i+1]]`` and their
            corresponding values are stored in ``data[indptr[i]:indptr[i+1]]``.
            If the shape parameter is not supplied, the matrix dimensions
            are inferred from the index arrays.

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
        CSR format data array of the matrix
    indices
        CSR format index array of the matrix
    indptr
        CSR format index pointer array of the matrix
    has_sorted_indices
        Whether indices are sorted

    Notes
    -----

    Sparse matrices can be used in arithmetic operations: they support
    addition, subtraction, multiplication, division, and matrix power.

    Advantages of the CSR format
      - efficient arithmetic operations CSR + CSR, CSR * CSR, etc.
      - efficient row slicing
      - fast matrix vector products

    Disadvantages of the CSR format
      - slow column slicing operations (consider CSC)
      - changes to the sparsity structure are expensive (consider LIL or DOK)

    Examples
    --------

    >>> import numpy as np
    >>> from scipy.sparse import csr_matrix
    >>> csr_matrix((3, 4), dtype=np.int8).toarray()
    array([[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]], dtype=int8)

    >>> row = np.array([0, 0, 1, 2, 2, 2])
    >>> col = np.array([0, 2, 2, 0, 1, 2])
    >>> data = np.array([1, 2, 3, 4, 5, 6])
    >>> csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
    array([[1, 0, 2],
           [0, 0, 3],
           [4, 5, 6]])

    >>> indptr = np.array([0, 2, 3, 6])
    >>> indices = np.array([0, 2, 2, 0, 1, 2])
    >>> data = np.array([1, 2, 3, 4, 5, 6])
    >>> csr_matrix((data, indices, indptr), shape=(3, 3)).toarray()
    array([[1, 0, 2],
           [0, 0, 3],
           [4, 5, 6]])

    Duplicate entries are summed together:

    >>> row = np.array([0, 1, 2, 0])
    >>> col = np.array([0, 1, 1, 0])
    >>> data = np.array([1, 2, 4, 8])
    >>> csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
    array([[9, 0, 0],
           [0, 2, 0],
           [0, 4, 0]])

    As an example of how to construct a CSR matrix incrementally,
    the following snippet builds a term-document matrix from texts:

    >>> docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
    >>> indptr = [0]
    >>> indices = []
    >>> data = []
    >>> vocabulary = {}
    >>> for d in docs:
    ...     for term in d:
    ...         index = vocabulary.setdefault(term, len(vocabulary))
    ...         indices.append(index)
    ...         data.append(1)
    ...     indptr.append(len(indices))
    ...
    >>> csr_matrix((data, indices, indptr), dtype=int).toarray()
    array([[2, 1, 0, 0],
           [0, 1, 1, 1]])

    """
    format = ...
    def transpose(self, axes=..., copy=...) -> csc_matrix:
        ...
    
    def tolil(self, copy=...) -> lil_matrix:
        ...
    
    def tocsr(self, copy=...) -> "csr_matrix":
        ...
    
    def tocsc(self, copy=...) -> csc_matrix:
        ...
    
    def tobsr(self, blocksize=..., copy=...) -> bsr_matrix:
        ...
    
    def __iter__(self) -> Generator[csr_matrix, None, None]:
        ...
    
    def getrow(self, i) -> "csr_matrix":
        """Returns a copy of row i of the matrix, as a (1 x n)
        CSR matrix (row vector).
        """
        ...
    
    def getcol(self, i) -> "csr_matrix":
        """Returns a copy of column i of the matrix, as a (m x 1)
        CSR matrix (column vector).
        """
        ...
    


def isspmatrix_csr(x) -> bool:
    """Is x of csr_matrix type?

    Parameters
    ----------
    x
        object to check for being a csr matrix

    Returns
    -------
    bool
        True if x is a csr matrix, False otherwise

    Examples
    --------
    >>> from scipy.sparse import csr_matrix, isspmatrix_csr
    >>> isspmatrix_csr(csr_matrix([[5]]))
    True

    >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc
    >>> isspmatrix_csr(csc_matrix([[5]]))
    False
    """
    ...

