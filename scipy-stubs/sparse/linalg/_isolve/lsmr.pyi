"""
This type stub file was generated by pyright.
"""

"""
Copyright (C) 2010 David Fong and Michael Saunders

LSMR uses an iterative method.

07 Jun 2010: Documentation updated
03 Jun 2010: First release version in Python

David Chin-lung Fong            clfong@stanford.edu
Institute for Computational and Mathematical Engineering
Stanford University

Michael Saunders                saunders@stanford.edu
Systems Optimization Laboratory
Dept of MS&E, Stanford University.

"""
__all__ = ['lsmr']
def lsmr(A, b, damp=..., atol=..., btol=..., conlim=..., maxiter=..., show=..., x0=...):
    """Iterative solver for least-squares problems.

    lsmr solves the system of linear equations ``Ax = b``. If the system
    is inconsistent, it solves the least-squares problem ``min ||b - Ax||_2``.
    ``A`` is a rectangular matrix of dimension m-by-n, where all cases are
    allowed: m = n, m > n, or m < n. ``b`` is a vector of length m.
    The matrix A may be dense or sparse (usually sparse).

    Parameters
    ----------
    A : {sparse matrix, ndarray, LinearOperator}
        Matrix A in the linear system.
        Alternatively, ``A`` can be a linear operator which can
        produce ``Ax`` and ``A^H x`` using, e.g.,
        ``scipy.sparse.linalg.LinearOperator``.
    b : array_like, shape (m,)
        Vector ``b`` in the linear system.
    damp : float
        Damping factor for regularized least-squares. `lsmr` solves
        the regularized least-squares problem::

         min ||(b) - (  A   )x||
             ||(0)   (damp*I) ||_2

        where damp is a scalar.  If damp is None or 0, the system
        is solved without regularization. Default is 0.
    atol, btol : float, optional
        Stopping tolerances. `lsmr` continues iterations until a
        certain backward error estimate is smaller than some quantity
        depending on atol and btol.  Let ``r = b - Ax`` be the
        residual vector for the current approximate solution ``x``.
        If ``Ax = b`` seems to be consistent, `lsmr` terminates
        when ``norm(r) <= atol * norm(A) * norm(x) + btol * norm(b)``.
        Otherwise, `lsmr` terminates when ``norm(A^H r) <=
        atol * norm(A) * norm(r)``.  If both tolerances are 1.0e-6 (default),
        the final ``norm(r)`` should be accurate to about 6
        digits. (The final ``x`` will usually have fewer correct digits,
        depending on ``cond(A)`` and the size of LAMBDA.)  If `atol`
        or `btol` is None, a default value of 1.0e-6 will be used.
        Ideally, they should be estimates of the relative error in the
        entries of ``A`` and ``b`` respectively.  For example, if the entries
        of ``A`` have 7 correct digits, set ``atol = 1e-7``. This prevents
        the algorithm from doing unnecessary work beyond the
        uncertainty of the input data.
    conlim : float, optional
        `lsmr` terminates if an estimate of ``cond(A)`` exceeds
        `conlim`.  For compatible systems ``Ax = b``, conlim could be
        as large as 1.0e+12 (say).  For least-squares problems,
        `conlim` should be less than 1.0e+8. If `conlim` is None, the
        default value is 1e+8.  Maximum precision can be obtained by
        setting ``atol = btol = conlim = 0``, but the number of
        iterations may then be excessive. Default is 1e8.
    maxiter : int, optional
        `lsmr` terminates if the number of iterations reaches
        `maxiter`.  The default is ``maxiter = min(m, n)``.  For
        ill-conditioned systems, a larger value of `maxiter` may be
        needed. Default is False.
    show : bool, optional
        Print iterations logs if ``show=True``. Default is False.
    x0 : array_like, shape (n,), optional
        Initial guess of ``x``, if None zeros are used. Default is None.

        .. versionadded:: 1.0.0

    Returns
    -------
    x : ndarray of float
        Least-square solution returned.
    istop : int
        istop gives the reason for stopping::

          istop   = 0 means x=0 is a solution.  If x0 was given, then x=x0 is a
                      solution.
                  = 1 means x is an approximate solution to A@x = B,
                      according to atol and btol.
                  = 2 means x approximately solves the least-squares problem
                      according to atol.
                  = 3 means COND(A) seems to be greater than CONLIM.
                  = 4 is the same as 1 with atol = btol = eps (machine
                      precision)
                  = 5 is the same as 2 with atol = eps.
                  = 6 is the same as 3 with CONLIM = 1/eps.
                  = 7 means ITN reached maxiter before the other stopping
                      conditions were satisfied.

    itn : int
        Number of iterations used.
    normr : float
        ``norm(b-Ax)``
    normar : float
        ``norm(A^H (b - Ax))``
    norma : float
        ``norm(A)``
    conda : float
        Condition number of A.
    normx : float
        ``norm(x)``

    Notes
    -----

    .. versionadded:: 0.11.0

    References
    ----------
    .. [1] D. C.-L. Fong and M. A. Saunders,
           "LSMR: An iterative algorithm for sparse least-squares problems",
           SIAM J. Sci. Comput., vol. 33, pp. 2950-2971, 2011.
           :arxiv:`1006.0758`
    .. [2] LSMR Software, https://web.stanford.edu/group/SOL/software/lsmr/

    Examples
    --------
    >>> from scipy.sparse import csc_matrix
    >>> from scipy.sparse.linalg import lsmr
    >>> A = csc_matrix([[1., 0.], [1., 1.], [0., 1.]], dtype=float)

    The first example has the trivial solution ``[0, 0]``

    >>> b = np.array([0., 0., 0.], dtype=float)
    >>> x, istop, itn, normr = lsmr(A, b)[:4]
    >>> istop
    0
    >>> x
    array([0., 0.])

    The stopping code `istop=0` returned indicates that a vector of zeros was
    found as a solution. The returned solution `x` indeed contains
    ``[0., 0.]``. The next example has a non-trivial solution:

    >>> b = np.array([1., 0., -1.], dtype=float)
    >>> x, istop, itn, normr = lsmr(A, b)[:4]
    >>> istop
    1
    >>> x
    array([ 1., -1.])
    >>> itn
    1
    >>> normr
    4.440892098500627e-16

    As indicated by `istop=1`, `lsmr` found a solution obeying the tolerance
    limits. The given solution ``[1., -1.]`` obviously solves the equation. The
    remaining return values include information about the number of iterations
    (`itn=1`) and the remaining difference of left and right side of the solved
    equation.
    The final example demonstrates the behavior in the case where there is no
    solution for the equation:

    >>> b = np.array([1., 0.01, -1.], dtype=float)
    >>> x, istop, itn, normr = lsmr(A, b)[:4]
    >>> istop
    2
    >>> x
    array([ 1.00333333, -0.99666667])
    >>> A.dot(x)-b
    array([ 0.00333333, -0.00333333,  0.00333333])
    >>> normr
    0.005773502691896255

    `istop` indicates that the system is inconsistent and thus `x` is rather an
    approximate solution to the corresponding least-squares problem. `normr`
    contains the minimal distance that was found.
    """
    ...

