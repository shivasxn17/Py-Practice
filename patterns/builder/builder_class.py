class SomeBuilder():
    # constants to be set

    """thats builder class"""

    def __init__(self,
                 some_common_attr="default value",
                 some_common_attr_2="default value 2"
                 ):
        self.some_common_attr = some_common_attr
        self.some_common_attr_2 = some_common_attr_2

    def item():
        return SomeBuilder()

    def with_some_common_attr(self, ur_val):
        print("some_common_attr is requested")
        self.some_common_attr = ur_val
        return self

    def with_some_common_attr_2(self, ur_val):
        print("some_common_attr_2 is requested")
        self.some_common_attr_2 = ur_val
        return self

    def build_whatever_type(self):
        print("producing of whatever_type which only needs some_common_attr")
        return SomeBuilder(some_common_attr=self.some_common_attr)

    def build_whatever_type_2(self):
        print("producing of whatever_type which only needs some_common_attr")
        return SomeBuilder(
            some_common_attr=self.some_common_attr,
            some_common_attr_2=self.some_common_attr_2
        )
