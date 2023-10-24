def build_xml_element(tag, content, **kwargs):
    result = f"<{tag}"
    for key, value in kwargs.items():
        result += f' {key}="{value} \ "'
    result += f"> {content} "
    return result


r = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(r)


