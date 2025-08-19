from tests.test_create_user import create_user
from tests.test_get_users import get_users
from tests.test_transfer import create_transfer


create_user({"name": "user", "email": "some@mail.org", })
create_user({"name": "user22", "email": "some22@mail.org", })

get_users()

create_transfer({"from_user_id": "1", "to_user_id": "2", "amount": "10",})
