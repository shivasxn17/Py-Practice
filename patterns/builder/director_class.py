from builder_class import SomeBuilder


class SomeDirector():
    """docstring for SomeDirector"""
    def build_some_special_type():
        return (
            SomeBuilder.item()
            .with_some_common_attr("my_val")
            .with_some_common_attr_2("another_val")
            .build_whatever_type()
        )


SomeDirector.build_some_special_type()

"""
***** OUTPUT *****
*some_common_attr is requested
some_common_attr_2 is requested
producing of whatever_type which only needs some_common_attr
"""
