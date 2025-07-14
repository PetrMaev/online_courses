import stripe
from config.settings import STRIPE_API_KEY
from materials.models import Course, Lesson

stripe.api_key = STRIPE_API_KEY


def create_stripe_course_product(course_id):
    """Создание продукта-курса на страйпе."""

    course = Course.objects.get(id=course_id)
    product = stripe.Product.create(name=course.title)
    return product


def create_stripe_lesson_product(lesson_id):
    """Создание продукта-урока на страйпе."""

    lesson = Lesson.objects.get(id=lesson_id)
    product = stripe.Product.create(name=lesson.title)
    return product


def create_stripe_price(amount, product):
    """Создание цены на страйпе."""

    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": product.get("name")},
    )
    return price


def create_stripe_session(price):
    """Создание сессии на оплату на страйпе."""

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
