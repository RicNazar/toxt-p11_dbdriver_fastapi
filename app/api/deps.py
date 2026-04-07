from typing import Annotated

from fastapi import Depends

from app.core.security import verify_token

# Reusable dependency alias for authenticated routes
AuthDep = Annotated[str, Depends(verify_token)]
