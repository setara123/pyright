# This sample tests a complex combination of TypeVarTuple,
# unpacking, bidirectional type inference, and recursive calls.

from typing import TypeVar, TypeVarTuple, Callable

X = TypeVar("X")
Y = TypeVar("Y")
Xs = TypeVarTuple("Xs")
Ys = TypeVarTuple("Ys")


def nil() -> tuple[()]:
    return ()


def cons(
    f: Callable[[X], Y],
    g: Callable[[*Xs], tuple[*Ys]],
) -> Callable[[X, *Xs], tuple[Y, *Ys]]:
    def wrapped(x: X, *xs: *Xs) -> tuple[Y, *Ys]:
        y, ys = f(x), g(*xs)
        return y, *ys

    return wrapped


def star(f: Callable[[X], Y]) -> Callable[[*tuple[X, ...]], tuple[Y, ...]]:
    def wrapped(*xs: X):
        if not xs:
            return nil()
        return cons(f, star(f))(*xs)

    return wrapped
