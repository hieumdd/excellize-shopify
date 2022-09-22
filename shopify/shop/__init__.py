import os

from shopify.shop import interface


shops = {
    i.shop_url: i
    for i in [
        interface.Shop(
            "VertaDente",
            "mannenwinkel-nl",
            os.getenv("VERDA_DENTE_TOKEN", ""),
        ),
        interface.Shop(
            "CaraCamilla",
            "caracamilla",
            os.getenv("CARACAMILLA_TOKEN", ""),
        ),
        interface.Shop(
            "BestiesOnTour",
            "bestiesontour",
            os.getenv("BESTIESONTOUR_TOKEN", ""),
        ),
    ]
}
