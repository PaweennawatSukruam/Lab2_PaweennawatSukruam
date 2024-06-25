import pytest
import source.print_promotion as print_promo

def test_print_promotion_150():
    result = print_promo.print_promotion(150)
    assert result == "Thank you and see you next time"

def test_print_promotion_0():
    result = print_promo.print_promotion(0)
    assert result == "Thank you and see you next time"
    
def test_print_promotion__100():
    result = print_promo.print_promotion(-1)
    assert result == "Thank you and see you next time"
    
def test_print_promotion_500():
    result = print_promo.print_promotion(500)
    assert result == "Free ice cream cone = 1"
    
def test_print_promotion_700():
    result = print_promo.print_promotion(700)
    assert result == "Free chocolate cake = 1"
    
def test_print_promotion_1200():
    result = print_promo.print_promotion(1200)
    assert result == "Free ice cream cone = 1 and Free chocolate cake = 1"
    
def test_print_promotion_1500():
    result = print_promo.print_promotion(1500)
    assert result == "Free ice cream cone = 1 and Free chocolate cake = 1"
    
def test_print_promotion_1700():
    result = print_promo.print_promotion(1700)
    assert result == "Free ice cream cone = 2 and Free chocolate cake = 1"
    
def test_print_promotion_2400():
    result = print_promo.print_promotion(2400)
    assert result == "Free ice cream cone = 2 and Free chocolate cake = 2"
    
def test_print_promotion_3100():
    result = print_promo.print_promotion(3100)
    assert result == "Free ice cream cone = 2 and Free chocolate cake = 3"