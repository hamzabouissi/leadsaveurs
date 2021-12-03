from django.urls import path
from rest_framework.routers import DefaultRouter
from leadsaveurs.searcher.views import MissionReclamationView
from leadsaveurs.users.views import (
    SaverView, UserSavedView, DonationView, UserViewSet,
)
app_name = "users"


router = DefaultRouter()
router.register("users",UserViewSet,"users")
router.register("savers",SaverView,"savers")
router.register("users_saved",UserSavedView,"usersaved")
router.register("donations",DonationView,"donations")
router.register("mission_reclamation",MissionReclamationView,"donations")
urlpatterns = [
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
] + router.urls
