
def validate_dict(rules, d):
    for key, prefix, middle, suffix in rules:
        if key in d:
            value = d[key]
            if not value.startswith(prefix) or not value.endswith(suffix) or middle not in value[1:-1]:
                return False
        else:
            return False

    return True


s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
print(validate_dict(s, d))