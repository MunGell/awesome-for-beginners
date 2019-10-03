def allowed_dating_age(my_age):
    girls_age = my_age/2 +7
    return girls_age

Jack_limit = allowed_dating_age(20)
Ron_limit = allowed_dating_age(45)
print("Jack can date girls", Jack_limit, "or older than this age")
print("Ron can date girls", Ron_limit, "or older than this age")