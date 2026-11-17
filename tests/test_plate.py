"""Лаб 12: AI бичсэн normalize_plate()-ийг тестээр баталгаажуулна (Arrange-Act-Assert)."""
import pytest

from suh.plate import normalize_plate


# ---- хэвийн тохиолдол
def test_canonical_plate_is_unchanged():
    # Arrange
    raw = "0123 УБА"
    # Act
    result = normalize_plate(raw)
    # Assert
    assert result == "0123 УБА"


@pytest.mark.parametrize("raw", ["0123уба", " 0123  УБА ", "0123УБА", "0123\tуба", "0123 УБА", "0123 УБА\n"])
def test_spacing_and_case_are_normalized(raw):
    # Arrange: жижиг үсэг, хоосон зайгүй, олон зай, таб, NBSP, мөр шилжилт
    # Act
    result = normalize_plate(raw)
    # Assert
    assert result == "0123 УБА"


def test_mongolian_letters_are_accepted():
    # Arrange: Ө, Ү, Ё нь [А-Я] мужид ордоггүй тул тусад нь шалгана
    raw = "5678 өүё"
    # Act
    result = normalize_plate(raw)
    # Assert
    assert result == "5678 ӨҮЁ"


# ---- хилийн тохиолдол, аюулгүй байдал (UNIQUE баганыг тойрохгүй)
@pytest.mark.parametrize("raw", ["０１２３ УБА", "٠١٢٣ УБА", "᠐᠑᠒᠓ УБА"])
def test_non_ascii_digits_are_rejected(raw):
    # Arrange: бүтэн өргөнтэй, араб, монгол бичгийн цифр
    # Act, Assert
    with pytest.raises(ValueError, match="стандарт бус цифр"):
        normalize_plate(raw)


@pytest.mark.parametrize("raw", ["0123 УБA", "0123 YБА", "0123 UBA"])
def test_latin_lookalike_letters_are_rejected(raw):
    # Arrange: кирилл үсэгтэй адилхан харагддаг латин A, Y
    # Act, Assert
    with pytest.raises(ValueError, match="латин үсэг"):
        normalize_plate(raw)


def test_old_cyrillic_variant_is_not_turned_into_valid_letter():
    # Arrange: «ᲀ» (U+1C80).upper() == «В» тул upper()-ээс өмнө шалгах ёстой
    raw = "0123 ᲀОС"
    # Act, Assert
    with pytest.raises(ValueError, match="хэлбэр буруу"):
        normalize_plate(raw)


@pytest.mark.parametrize("raw", ["", "123 УБА", "12345 УБА", "0123 УБ", "0123 УБАА", "УБА 0123"])
def test_wrong_shape_is_rejected(raw):
    # Arrange: хоосон, цифр дутуу/илүү, үсэг дутуу/илүү, дараалал буруу
    # Act, Assert
    with pytest.raises(ValueError, match="хэлбэр буруу"):
        normalize_plate(raw)


def test_too_long_input_is_rejected_before_regex():
    # Arrange: 21 тэмдэгт
    raw = "0123" + " " * 14 + "УБА"
    # Act, Assert
    with pytest.raises(ValueError, match="20 тэмдэгтээс урт"):
        normalize_plate(raw)


@pytest.mark.parametrize("raw", [None, 123, b"0123 \xd0\xa3"])
def test_non_string_is_rejected(raw):
    # Arrange: str биш оролт
    # Act, Assert
    with pytest.raises(TypeError):
        normalize_plate(raw)
