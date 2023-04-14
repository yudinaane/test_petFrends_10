from api import PetFriends
from settings import valid_email, valid_password, no_valid_email, no_valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data (name='Almaz', animal_type='malamut',
                                    age='5', pet_photo=r'images\Alaskan_Malamute.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Almaz', 'malamut', '5', r'images\Alaskan_Malamute.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Ydja', animal_type='shpiz', age='5'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


def test_add_new_pet_simple_with_valid_data(name='Pluton', animal_type='dzhekraasel', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_add_photo_pet_valid_format(pet_photo=r'sobaka.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        if my_pets['pet_photo'] is None:
            status, result = pf.add_photo_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
            assert status == 200
            assert result['pet_photo'] is not None
        else:
            raise Exception("Pet has a photo")
    else:
        raise Exception("There is no my pets")



def test_get_api_key_for_NO_valid_user_1(email=valid_email, password=no_valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' is not result

def test_get_api_key_for_NO_valid_user_2(email=no_valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' is not result

def test_get_all_pets_with_NO_valid_key_str_3(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets_NO_VALID_KEY_str(auth_key, filter)
    assert status == 403
    assert 'pets' is not result

def test_get_all_pets_with_NO_valid_key_int_4(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets_NO_VALID_KEY_int(auth_key, filter)
    assert status == 403
    assert 'pets' is not result

def test_get_all_pets_with_valid_key_NO_VALID_FILTER_5(filter='pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 500

def test_POST_api_key_for_valid_user_NO_valid_method_6(email=valid_email, password=valid_password):
    status, result = pf.post_api_key(email, password)
    assert status == 405
    assert 'key' is not result

def test_successful_update_self_pet_info_NO_valid_method_7(name='Ydja', animal_type='shpiz', age='5'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.post_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 405
        assert 'name' is not result
    else:
        raise Exception("There is no my pets")

def test_add_new_pet_simple_with_NO_valid_age_8(name='Rex', animal_type='boxer', age= '的一是不了人我在有他这为之大来以个中上们'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 400
    assert 'age' is not result


def test_add_new_pet_simple_with_NO_valid_name_9(name='|\\/!@#$%^&*()-_=+`~?\"№;:[]{}', animal_type='bigl', age='1'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 400
    assert 'name' is not result


def test_add_new_pet_simple_with_NO_valid_animal_type_10(name='Vasy', animal_type='Текстовое поле в приложении кажется таким обычным делом, однако это одна из наиболее важных вещей, которую мы можем протестировать. Почему? Потому что текстовые поля дают доступ к приложению и его базе данных. Валидация текстового поля – это то, что предотвращает появление в базе плохих данных. Эти данные могут вызвать разнообразные проблемы для пользователей и разработчиков. Валидация также предотвращает атаки межсайтового скриптинга и SQL-инъекции.', age='8'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 400
    assert 'name' is not result


