from fastapi import APIRouter, Depends, HTTPException, status

from ..cruds import auth_crud

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router_auth = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router_auth.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    user = auth_crud.verify_password(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas"
        )

    access_token = auth_crud.create_access_token(form_data.username)
    return {"access_token": access_token, "token_type": "bearer"}
