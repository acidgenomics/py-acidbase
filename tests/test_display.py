"""Tests for acidbase._display."""

from acidbase import show_header, show_slot_info, simple_class


class TestSimpleClass:
    """Tests for simple_class."""

    def test_builtin(self) -> None:
        """Returns builtin type names."""
        assert simple_class(42) == "int"
        assert simple_class("hi") == "str"

    def test_custom(self) -> None:
        """Returns custom class name."""

        class Foo:
            pass

        assert simple_class(Foo()) == "Foo"


class TestShowHeader:
    """Tests for show_header."""

    def test_basic(self) -> None:
        """Header contains label and has fixed width."""
        h = show_header("Test")
        assert "Test" in h
        assert len(h) == 72


class TestShowSlotInfo:
    """Tests for show_slot_info."""

    def test_basic(self) -> None:
        """Returns slot names and types for object."""

        class Example:
            def __init__(self) -> None:
                self.name = "test"
                self.value = 42

        result = show_slot_info(Example())
        assert "name" in result
        assert "str" in result
        assert "value" in result
        assert "int" in result
