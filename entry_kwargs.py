def entry(name, gender, **kwargs) :
    data = dict()
    data.setdefault("name", name)
    data.setdefault("gender", gender)
    data.update(kwargs)
    print(data)

entry(name="大山坂道", gender="男性", age=27, course="E")