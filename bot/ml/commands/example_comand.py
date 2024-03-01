class Example_command:
    def __init__(self):
        # deps
        pass

    def run(self, user_data, tokens):
        return (
            f"tipo json {user_data.get_data()} {list(map(lambda x: x['word'],tokens))}"
        )
