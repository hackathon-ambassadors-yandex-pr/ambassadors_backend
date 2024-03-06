from apps.api.v1.drf_spectacular.sendings.view_decorators import (
    SENDINGS_VIEW_DECORATORS,
)
from apps.api.v1.drf_spectacular.tokens.view_decorators import TOKENS_VIEW_DECORATORS
from apps.api.v1.drf_spectacular.users.view_decorators import USERS_VIEW_DECORATORS

VIEW_DECORATORS = {
    "tokens": TOKENS_VIEW_DECORATORS,
    "users": USERS_VIEW_DECORATORS,
    "sendings": SENDINGS_VIEW_DECORATORS,
}
