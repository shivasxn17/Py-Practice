import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Input(id="input_id", value="enter some value", type="text"),
    html.Div(id="output_id")
])


@app.callback(
	Output(component_id="output_id", component_property="children"),
	[Input(component_id="input_id", component_property="value")]
)
def update_on_output(input_value):
	try:
		sample_lookup = {
			"1":"yo",
			"2":"yolo"
		}
		return f"found it {sample_lookup[input_value]}"
	except Exception as e:
		return "not found ur id"


if __name__ == '__main__':
    app.run_server(debug=True)