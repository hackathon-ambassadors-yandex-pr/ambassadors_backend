from apps.api.v1.drf_spectacular.ambassadors.view_decorators import (
    AMBASSADORS_VIEW_DECORATORS,
)
from apps.api.v1.drf_spectacular.sendings.view_decorators import (
    SENDINGS_VIEW_DECORATORS,
)
from apps.api.v1.drf_spectacular.tokens.view_decorators import TOKENS_VIEW_DECORATORS
from apps.api.v1.drf_spectacular.users.view_decorators import USERS_VIEW_DECORATORS
from apps.api.v1.drf_spectacular.yandex_forms.view_decorators import (
    YANDEX_FORMS_VIEW_DECORATORS,
)

VIEW_DECORATORS = {
    "tokens": TOKENS_VIEW_DECORATORS,
    "users": USERS_VIEW_DECORATORS,
    "sendings": SENDINGS_VIEW_DECORATORS,
    "yandex_forms": YANDEX_FORMS_VIEW_DECORATORS,
    "ambassadors": AMBASSADORS_VIEW_DECORATORS,
}
