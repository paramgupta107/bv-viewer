from IPython.display import IFrame
from pathlib import Path


def display_bv_string(bv_text, width=800, height=400):
    """
    Display a bv file with the content of the bv file in a string.

    Args:
        bv_text (str): The content of the bv file as a string.
        width (int): Width of the display frame.
        height (int): Height of the display frame.
    """
    html_code = f"""
    <!DOCTYPE html>
<html lang="en-us">
  <head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="IE=edge" />

	<title>BV.js</title>
	<meta name="description" content="">
	<meta name="author" content="Saleh Dindar">
	<link rel="shortcut icon" href="favicon.ico">
	
	<style>
		html, body {{ overscroll-behavior: none; }}

		div#ui-brand {{
	z-index: 3;
	position: absolute;
	top: 0;
	left: 0;
	height: 30px;
	width: 100%;
	font-size: 18pt;
	padding: 6px;
}}

a#bar-menu {{
	margin: 4px;
}}



#ui-panel {{
	position: absolute;
	left: 0;
	top: 0;
	padding: 5px;
	opacity: 0.8;
	width: 100%;
	z-index:100;
	background-color: #ecf0f1;
}}

#ui-panel .program-name {{
	font-size:18pt;
	font-weight: bold;
}}

#ui-panel .top-level > a {{
	opacity: 1.0;
	color: black;
	font-size: 16pt;
	text-decoration: underline;
	padding-left: 8px;
	padding-right: 8px;
}}

#ui-panel .top-level > a:hover {{
	color: white;
	background-color: black;
	font-size: 16pt;
	text-decoration: none;
}}

#ui-panel .bottom-level {{
	display:none;
	padding-top:20px;
	padding-bottom:20px;
}}

#ui-panel div {{
	padding: 5px;
}}

a.checked i.check {{
	visibility: visible;
}}
a i.check {{
	visibility: hidden;
}}
#ui-panel > * {{
	opacity: 1.0;
}}
.navbar .fa {{
	font-size: 130%;
}}
canvas#drawing {{
	position: absolute;
	top: 0;
	left: 0;
	cursor: default;
	width: 100%;
	height: 100%;
}}

.navbar-header img {{
	float: left;
	height: 40px;
	margin:2.5px 5px;
}}

.fieldset {{
	display: inline-block;
	border-top: solid 1px black;
	vertical-align: top;
	margin: 5px;
}}

.legend {{
	font-weight: bold;
}}

body {{
	overflow: hidden;
	margin: 0;
	padding: 0;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	background-repeat: repeat;
}}

.noselect {{
	user-select: none;
	-ms-user-select: none;
	-moz-user-select: none;
	-khtml-user-select: none;
	-webkit-user-select: none;
	-webkit-touch-callout: none;
}}

.which-group-am-i-changing {{
	font-style: italic;
	width: 200px;
}}
	</style>
  </head>
  <body>
	<div id="ui-panel">
		<span class="program-name">BezierView.js</span>
		<span class="top-level">
			<a id="top-level-shader-settings" href="#">Shader Settings</a>
		</span>
		<span class="top-level">
			<a id="top-level-curvature" href="#">Curvature</a>
		</span>
		<span class="top-level">
			<a id="top-level-display" href="#">Display</a>
		</span>
		<span class="top-level">
			<a id="top-level-groups" href="#">Groups</a>
		</span>
		<span class="top-level">
			<a id="top-level-other" href="#">Other</a>
		</span>
		<span class="top-level">
			<a id="top-level-help" href="#">Help</a>
		</span>

		<div id="bottom-level-shader-settings" class="bottom-level">
			<div class="fieldset">
				<div>
					<label>
						<input type="checkbox" id="check-flip-normals"/> Flip Normals
					</label>
				</div>
				<div>
					<label>
						<input type="checkbox" id="check-flat-shading"/> Flat Shading
					</label>
				</div>
				<div>
					<label>
						<input type="checkbox" id="check-highlight"/> Highlight Lines
					</label>
				</div>
				<div>
					<label>
						<input type="checkbox" id="check-reflection"/> Highlight Reflection
					</label>
				</div>
				<div>
					<label>
						<input type="checkbox" id="check-wireframe"/> Wireframe
					</label>
				</div>
				<div>
					<label>
						<input type="checkbox" id="check-visualize_normals"/> Visualize Normals
					</label>
				</div>
				<div class="which-group-am-i-changing"></div>
			</div>
			<div class="fieldset">
				<div>
					<label>
						Highlight Density<input type="range" min="0" max="1" value="0.5" step="0.05" id="range-highlight-density">
						<span id="range-highlight-density-value">0.5</span>
					</label>
				</div>
				<div>
					<label>
						Highlight Resolution<input type="range" min="0" max="30" value="10" step="0.1" id="range-highlight-resolution">
						<span id="range-highlight-resolution-value">10.0</span>
					</label>
				</div>
				<div>
					<label>
						Vizualize Normal Size<input type="range" min="0.01" max="10" value="1" step="0.01" id="range-visual-normal-size">
						<span id="range-visual-normal-size-value">1.0</span>
					</label>
				</div>
			</div>
		</div>

		<div id="bottom-level-curvature" class="bottom-level">
			<div class="fieldset">
				<div>
					<label>
						<input type="checkbox" id="check-curvature"/> Show Curvature
					</label>
				</div>
				<div>
					<label for="select-curv-type">Curvature Type</label>
					<select id="select-curv-type">
						<option value="0">Gaussian</option>
						<option value="1">Mean</option>
						<option value="2">Max</option>
						<option value="3">Min</option>
					</select>
				</div>
				<div class="which-group-am-i-changing"></div>
			</div>
			<div class="fieldset">
				<div class="legend">Curvature values</div>
				<div>
					min: <span id="min-crv-actual">--</span>
				</div>
				<div>
					max: <span id="max-crv-actual">--</span>
				</div>
			</div>
			<div class="fieldset">
				<div class="legend">Curvature clamp</div>
				<div>
					<label>
						min
						<input style="width: 100px" type="text" id="min-crv-in">
					</label>
				</div>
				<div>
					<label>
						max
						<input style="width: 100px" type="text" id="max-crv-in">
					</label>
				</div>
				<div>
					<button id="restore-crv-in" disabled>Reset</button>
				</div>
			</div>
		</div>

		<div id="bottom-level-display" class="bottom-level">
			<div class="fieldset">
				<div>
					<label>
						<input type="checkbox" id="check-control-mesh" /> Show Control Mesh
					</label>
				</div>
				<div>
					<label>
						<input type="checkbox" id="check-bounding-box" /> Show Bounding Box
					</label>
				</div>
				<div>
					<label>
						<input type="checkbox" id="check-patches" checked /> Show Patches
					</label>
				</div>
				<div class="which-group-am-i-changing"></div>
			</div>
			<div class="fieldset">
				<div class="legend">Lights</div>
				<div>
					<label>
						<input type="checkbox" id="check-light-1"/> Light 1
					</label>
				</div>
				<div>
					<label>
						<input type="checkbox" id="check-light-2"/> Light 2
					</label>
				</div>
				<div>
					<label>
						<input type="checkbox" id="check-light-3"/> Light 3
					</label>
				</div>
			</div>
			<div class="fieldset">
				<label for="select-patch-detail">Patch Detail</label>
				<select id="select-patch-detail">
					<option value="2">4 &times; 4</option>
					<option value="3">8 &times; 8</option>
					<option value="4">16 &times; 16</option>
					<option value="5">32 &times; 32</option>
					<option value="6">64 &times; 64</option> 
				</select>
			</div>
		</div>

		<div id="bottom-level-groups" class="bottom-level">
			<div class="fieldset">
				<div>
					<label for="select-group">Group</label>
					<select id="select-group">
					</select>
				</div>
				<div>
					<label for="select-group-color">Group Color</label>
					<select id="select-group-color">
					</select>
				</div>
				<div>
					<button id="delete-group">Delete Group</button>
				</div>
			</div>
		</div>

		<div id="bottom-level-other" class="bottom-level">
			<div class="fieldset">
				<div class="legend">Mouse Mode</div>
				<div>
					<input id="rotateModeTrue" type="radio" name="mouseMode" value="rotate" checked="">Rotate
				</div>
				<div>
					<input id="rotateModeFalse" type="radio" name="mouseMode" value="clip">Clip
				</div>
			</div>
			<div class="fieldset">
				<div class="legend">Saved Positions</div>
				<div>
					<button id="save-position">Save Position</button>
				</div>
				<div>
					<button id="remove-position">Remove Position</button>
				</div>
				<div>
					<label for="select-load-position">Load Position</label>
					<select id="select-load-position">
					</select>
				</div>
				<div>
					<button id="restore-load-position">Reload Current</button>
				</div>
			</div>
			<div class="fieldset">
				<button id="btn-reset">Reset Projection</button>
			</div>
		</div>

		<div id="bottom-level-help" class="bottom-level">
			<p><b> Controls </b><br>
			Left Mouse: Rotate or Clip <br>
			Right Mouse: Pan <br>
			Scroll Wheel: Zoom <br>
			Scroll Wheel + Alt: Scale <br>
			Q and E: Z-axis rotation <br>
			ESC: Reset projection <br></p>
			<p> BV files can also be loaded by dragging and dropping on this window </p>
			<p><b> About </b><br>
			This is an implementation of 
			<a href="http://www.cise.ufl.edu/research/SurfLab/bview/" target="_blank"> SurfLab's BezierView</a> using WebGL.<br>
			<a href="https://bitbucket.org/surflab/bv.js/" target="_blank"><i class="fa fa-bitbucket"></i> Source code</a></p>
		</div>
	</div>
	<canvas id="drawing"></canvas>

	<!--<script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>-->
	<!--<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>-->
	<script src="https://cdn.rawgit.com/eligrey/FileSaver.js/62d219a0fac54b94cd4f230e7bfc55aa3f8dcfa4/FileSaver.js"></script>
	<script>/*
		the Vec3 class does have a fourth element called 'd' that
		is the rational point and not considered a member
		(except for when it is normalized)
		*/
		var Vec3 = /** @class */ (function () {{
			function Vec3() {{
				this.x = 0;
				this.y = 0;
				this.z = 0;
				this.d = 1;
			}}
			Vec3.prototype.set = function (v0, v1, v2) {{
				this.x = v0;
				this.y = v1;
				this.z = v2;
				return this;
			}};
			Vec3.prototype.set4 = function (v0, v1, v2, v3) {{
				this.d = v3;
				return this.set(v0, v1, v2);
			}};
			Vec3.prototype.copy = function (v) {{
				this.x = v.x;
				this.y = v.y;
				this.z = v.z;
				this.d = v.d;
				return this;
			}};
			Vec3.prototype.dup = function () {{
				var ret = new Vec3();
				ret.set4(this.x, this.y, this.z, this.d);
				return ret;
			}};
			Vec3.prototype.add = function (v) {{
				this.x += v.x;
				this.y += v.y;
				this.z += v.z;
				return this;
			}};
			Vec3.prototype.add4 = function (v) {{
				this.d += v.d;
				return this.add(v);
			}};
			Vec3.prototype.sub = function (v) {{
				this.x -= v.x;
				this.y -= v.y;
				this.z -= v.z;
				return this;
			}};
			Vec3.prototype.sub4 = function (v) {{
				this.d -= v.d;
				return this.sub(v);
			}};
			Vec3.prototype.scale = function (s) {{
				this.x *= s;
				this.y *= s;
				this.z *= s;
				return this;
			}};
			Vec3.prototype.scale4 = function (s) {{
				this.d *= s;
				return this.scale(s);
			}};
			Vec3.prototype.cross = function (v) {{
				var my_x = this.x;
				var my_y = this.y;
				var my_z = this.z;
				this.x = my_y * v.z - my_z * v.y;
				this.y = my_z * v.x - my_x * v.z;
				this.z = my_x * v.y - my_y * v.x;
				this.d = 1;
				return this;
			}};
			Vec3.prototype.dot = function (v) {{
				return this.x * v.x + this.y * v.y + this.z * v.z;
			}};
			Vec3.prototype.dot4 = function (v) {{
				return this.x * v.x + this.y * v.y + this.z * v.z + this.d * v.d;
			}};
			Vec3.prototype.length = function () {{
				return Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z);
			}};
			Vec3.prototype.length4 = function () {{
				return Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z + this.d * this.d);
			}};
			Vec3.prototype.normalize = function () {{
				this.scale(1 / this.length());
				return this;
			}};
			Vec3.prototype.normalize4 = function () {{
				this.scale4(1 / this.length4());
				return this;
			}};
			Vec3.prototype.normalize_rational_point = function () {{
				if (this.d != 0) {{
					this.scale(1 / this.d);
					this.d = 1.0;
				}}
				return this;
			}};
			Vec3.prototype.toString = function () {{
				return '(' + this.x + ', ' + this.y + ', ' + this.z + '; ' + this.d + ')';
			}};
			// this is a right multiply of a quaternion
			// ie: v2 = this, v1 = q
			Vec3.prototype.quaternion_mul = function (q) {{
				var newD = q.d * this.d - q.dot(this);
				// v1, v2 represents the vector (imaginary) part of the quaternion
				// d1*v2 + d2*v1 + (v1 cross v2)
				var res = this.dup().scale(q.d).add(q.dup().scale(this.d)).add(q.dup().cross(this));
				res.d = newD;
				return this.copy(res);
			}};
			// sets the vector to represent a quaternion from an axis and angle
			Vec3.prototype.set_axis_angle = function (v0, v1, v2, theta) {{
				var c = Math.cos(theta / 2);
				var s = Math.sin(theta / 2);
				return this.set4(v0 * s, v1 * s, v2 * s, c);
			}};
			return Vec3;
		}}());
		function det4(x11, x12, x13, x14, x21, x22, x23, x24, x31, x32, x33, x34, x41, x42, x43, x44) {{
			return x11 * x22 * x33 * x44 - x11 * x22 * x34 * x43 - x11 * x32 * x23 * x44 + x11 * x32 * x24 * x43 + x11 * x42 * x23 * x34 - x11 * x42 * x24 * x33 - x21 * x12 * x33 * x44 + x21 * x12 * x34 * x43 + x21 * x32 * x13 * x44 - x21 * x32 * x14 * x43 - x21 * x42 * x13 * x34 + x21 * x42 * x14 * x33 + x31 * x12 * x23 * x44 - x31 * x12 * x24 * x43 - x31 * x22 * x13 * x44 + x31 * x22 * x14 * x43 + x31 * x42 * x13 * x24 - x31 * x42 * x14 * x23 - x41 * x12 * x23 * x34 + x41 * x12 * x24 * x33 + x41 * x22 * x13 * x34 - x41 * x22 * x14 * x33 - x41 * x32 * x13 * x24 + x41 * x32 * x14 * x23;
		}}
		function det3(x11, x12, x13, x21, x22, x23, x31, x32, x33) {{
			return x11 * x22 * x33 - x11 * x23 * x32 - x12 * x21 * x33 + x12 * x23 * x31 + x13 * x21 * x32 - x13 * x22 * x31;
		}}
	</script>
	<script>
	var PatchType;
		(function (PatchType) {{
			PatchType[PatchType["Triangle"] = 1] = "Triangle";
			PatchType[PatchType["Quadrilateral"] = 2] = "Quadrilateral";
			PatchType[PatchType["Polyhedral"] = 3] = "Polyhedral";
		}})(PatchType || (PatchType = {{}}));
		var Patch = /** @class */ (function () {{
			function Patch(kind, degu, degv, mesh) {{
				this.kind = kind;
				this.degu = degu;
				this.degv = degv;
				this.mesh = mesh;
				this.points = [];
				this.normals = [];
				this.curvature = [];
				this.artificial_normals = null;
				// only used for polyhedron data
				this.polyhedron_indices = [];
				this.polyhedron_edges = [];
			}}
			Patch.MakeQuad = function (degu, degv, mesh) {{
				return new Patch(PatchType.Quadrilateral, degu, degv, mesh);
			}};
			Patch.MakePolyhedral = function (points, indices, edges) {{
				var p = new Patch(PatchType.Polyhedral, 0, 0, points);
				p.polyhedron_indices = indices;
				p.polyhedron_edges = edges
				return p;
			}};
			Patch.MakeTriangle = function (deg, mesh) {{
				return new Patch(PatchType.Triangle, deg, deg, mesh);
			}};
			return Patch;
		}}());
		function bb_copy(p, step, bb) {{
			var C = step * p.degu + 1;
			for (var i = 0; i <= p.degu; ++i) {{
				for (var j = 0; j <= p.degv; ++j) {{
					var src = i * (p.degv + 1) + j;
					var dst = j * step * C + i * step;
					bb[dst].copy(p.mesh[src]);
				}}
			}}
		}}
		function subdivide_quad(p, step, sizeu, sizev, bb) {{
			var halfstep = step / 2;
			var bigstepu = step * p.degu;
			var bigstepv = step * p.degv;
			var C = sizeu + 1;
			// patch level
			for (var row = 0; row < sizev; row += bigstepv) {{
				for (var col = 0; col <= sizeu; col += step) {{
					// subdivide a curve-COLumn of degree degv
					for (var l = 0; l < p.degv; ++l) {{
						var h = row + l * halfstep;
						for (var k = l; k < p.degv; ++k) {{
							var h1 = h + step;
							var h2 = h + halfstep;
							var dst = h2 * C + col;
							var src0 = h * C + col;
							var src1 = h1 * C + col;
							// taking an average, ie:
							// bb[dst] = (bb[src0] + bb[src1]) / 2
							bb[dst].copy(bb[src0]).add4(bb[src1]).scale4(0.5);
							h = h1;
						}}
					}}
				}}
			}}
			// 2x patch level
			for (var col = 0; col < sizeu; col += bigstepu) {{
				for (var row = 0; row <= sizev; row += halfstep) {{
					// subdivide a curve-ROW of degree degu
					for (var l = 0; l < p.degu; ++l) {{
						var h = col + l * halfstep;
						for (var k = l; k < p.degu; ++k) {{
							var h1 = h + step;
							var h2 = h + halfstep;
							var dst = row * C + h2;
							var src0 = row * C + h;
							var src1 = row * C + h1;
							// taking an average, ie: 
							// bb[dst] = (bb[src0] + bb[src1]) / 2
							bb[dst].copy(bb[src0]).add4(bb[src1]).scale4(0.5);
							h = h1;
						}}
					}}
				}}
			}}
		}}
		function evaluate_quad(p, level) {{
			var step = 1 << level;
			var sizeu = step * p.degu;
			var sizev = step * p.degv;
			var C = step + 1;
			var Cu = sizeu + 1;
			var Cv = sizev + 1;
			p.points = [];
			p.normals = [];
			p.curvature = [];
			for (var i = 0; i < C * C; ++i) {{
				p.points.push(new Vec3());
				p.normals.push(new Vec3());
				p.curvature.push({{ gaussian: 0, mean: 0, max: 0, min: 0 }});
			}}
			var bb = [];
			for (var i = 0; i < Cu * Cv; ++i) {{
				bb.push(new Vec3());
			}}
			bb_copy(p, step, bb);   // JP check whether efficient in situ is being used
			for (var i = 0; i < level; ++i) {{
				subdivide_quad(p, step, sizeu, sizev, bb);
				step /= 2;
			}}
			// we know that the step should equal 1 at this point
			for (var r = 0; r < sizev; r += p.degv) {{
				var rs =       r * Cu;
				var r1 = (r + 1) * Cu;
				var r2 = (r + 2) * Cu;
				for (var c_1 = 0; c_1 < sizeu; c_1 += p.degu) {{
					var pi_1 = Math.floor(c_1 / p.degu) * C + Math.floor(r / p.degv);
				// pick 6 BB-coefficients in the lower left corners of large array
				// evaluate_at(p, pi, swap_degree, v00, v01, v02, v10, v20, v11) 
					evaluate_at(p, pi_1, false, bb[rs + c_1], bb[rs + c_1 + 1], bb[rs + c_1 + 2], bb[r1 + c_1], bb[r2 + c_1], bb[r1 + c_1 + 1]);
				}}
				// in the last column cannot take the values "up and to the right"
				// so we rotate our stencil 90 deg
				var c = sizeu;
				var pi = Math.floor(c / p.degu) * C + Math.floor(r / p.degv);
				evaluate_at(p, pi, true, bb[rs + c], bb[r1 + c], bb[r2 + c], bb[rs + c - 1], bb[rs + c - 2], bb[r1 + c - 1]);
			}}
			// for the top row
			{{
				var r = sizev;
				var rs = r * Cu;
				var r1 = (r - 1) * Cu;
				var r2 = (r - 2) * Cu;
				for (var c_2 = 0; c_2 < sizeu; c_2 += p.degu) {{
					var pi_2 = Math.floor(c_2 / p.degu) * C + Math.floor(r / p.degv);
					evaluate_at(p, pi_2, true, bb[rs + c_2], bb[r1 + c_2], bb[r2 + c_2], bb[rs + c_2 + 1], bb[rs + c_2 + 2], bb[r1 + c_2 + 1]);
				}}
				// for the top right
				var c = sizeu;
				var pi = Math.floor(c / p.degu) * C + Math.floor(r / p.degv);
				evaluate_at(p, pi, false, bb[rs + c], bb[rs + c - 1], bb[rs + c - 2], bb[r1 + c], bb[r2 + c], bb[r1 + c - 1]);
			}}
			if (p.artificial_normals) {{
				// buffers for decasteljau's algorithm
				var u_buffer = [];
				var v_buffer = [];
				for (var i = 0; i < p.artificial_normals.degu + 1; ++i) {{
					u_buffer.push(new Vec3());
				}}
				for (var i = 0; i < p.artificial_normals.degv + 1; ++i) {{
					v_buffer.push(new Vec3());
				}}
				var N = 1 << level;
				for (var r = 0; r <= N; ++r) {{
					// neither u nor v are integers
					var u = 1.0 - (r / N);
					for (var c = 0; c <= N; ++c) {{
						var v = 1.0 - (c / N);
						// DeCastel2(p->normal, p->Ndegu, p->Ndegv, u, v, p->eval_N[loc]);
						// perform a two dimensional decasteljau
						for (var i = 0; i <= p.artificial_normals.degu; ++i) {{
							for (var j = 0; j <= p.artificial_normals.degv; ++j) {{
								var index = i * (p.artificial_normals.degv + 1) + j;
								v_buffer[j].copy(p.artificial_normals.normals[index]);
							}}
							decastel_1(v_buffer, p.artificial_normals.degv, v, u_buffer[i]);
						}}
						var normal_index = r * C + c;
						decastel_1(u_buffer, p.artificial_normals.degu, u, p.normals[normal_index]);
						p.normals[normal_index].normalize();
					}}
				}}
			}}
		}}
		/*
		curvature and evaluation for four sided patch
		input: Bezier control points related to the curvature, the patch,
		and the index that we are writing to
		v ^
		  | v02
		  | v01 v11
		  | v00 v10 v20
		  +---------------> u
		output: curvature at v00, normal at v00
		*/
		function evaluate_at(p, pi, swap_degree, v00, v01, v02, v10, v20, v11) {{
			// p has position in R3, normal, curvature  whereas vij can be R4
			// JP: pi is index ???
			var degu = swap_degree ? p.degv : p.degu;
			var degv = swap_degree ? p.degu : p.degv;
			// DELME if (v00.y > 5) console.log("v00:", v00.x, v00.y, v00.z, v00.d);
			var v00p = v00.dup().normalize_rational_point();
			// DELME if (v00p.y > 5) console.log("v00p:", v00p.x, v00p.y, v00p.z, v00p.d);
			p.points[pi].copy(v00p);
			//p.points[pi].copy(v00).normalize_rational_point();
			// surface normal n = rv cross ru (but use a normalized derivative)
			// JP23: rational formula is deg d1/d0(v01-v00)
			{{
				//var ru_n = v01.dup().sub(v00.dup()).scale(degu);
				var v00n = v00.dup().normalize_rational_point();
				var ru_n = v01.dup().normalize_rational_point().sub(v00n);
				// var ru_n = v01.dup().normalize_rational_point().sub(v00.dup().normalize_rational_point());
				//var ru_n = v01.dup().normalize_rational_point().sub(v00.dup().normalize_rational_point()).scale(degu);
				if (ru_n.length() < 1e-6) {{
			   // when one edge is collapsed, use a different vector for the cross product
				   ru_n = v11.dup().normalize_rational_point().sub(v00n);
				   //ru_n = v11.dup().normalize_rational_point().sub(v00.dup().normalize_rational_point());
				}}
				// var rv_n = v10.dup().sub(v00.dup()).scale(degv);
				var rv_n = v10.dup().normalize_rational_point().sub(v00n);
				// var rv_n = v10.dup().normalize_rational_point().sub(v00.dup().normalize_rational_point());
				if (rv_n.length() < 1e-6) {{
					rv_n = v11.dup().normalize_rational_point().sub(v00n);
					//rv_n = v11.dup().normalize_rational_point().sub(v00.dup().normalize_rational_point());
				}}
				p.normals[pi].copy(rv_n).cross(ru_n).normalize();
			//console.log("N:", p.normals[pi].x, p.normals[pi].y, p.normals[pi].z)
				//p.normals[pi].copy(rv_n).cross(ru_n).normalize();
			}}
			// ru = degu*(v01 - v00)
			var ru = v01.dup().sub4(v00).scale4(degu);
			// rv = degv*(v10 - v00)
			var rv = v10.dup().sub4(v00).scale4(degv);
			var ruu = new Vec3();
			if (degu > 1) {{
				// ruu = (degu)*(degu - 1)*(v02 - 2*v01 + v00);
				ruu.copy(v02).sub4(v01).sub4(v01).add4(v00).scale4(degu).scale4(degu - 1);
			}}
			var rvv = new Vec3();
			if (degv > 1) {{
				// rvv = (degv)*(degv - 1)*(v20 - 2*v10 + v00)
				rvv.copy(v20).sub4(v10).sub4(v10).add4(v00).scale4(degv).scale4(degv - 1);
			}}
			var ruv = new Vec3();
			if (p.kind == PatchType.Triangle) {{
				if (p.degu > 1) {{
					// ruv = degu*(degu - 1)*(v11 - v01 - v10 + v00)
					ruv.copy(v11).sub4(v01).sub4(v10).add4(v00).scale4(degu).scale4(degu - 1);
				}}
			}}
			else {{
				// ruv = degu*degv*(v11 - v01 - v10 + v00)
				ruv.copy(v11).sub4(v01).sub4(v10).add4(v00).scale4(degu).scale4(degv);
			}}
			// coefficients of first and second fundamental form
			var L = det4(ruu.x, ruu.y, ruu.z, ruu.d, ru.x, ru.y, ru.z, ru.d, rv.x, rv.y, rv.z, rv.d, v00.x, v00.y, v00.z, v00.d);
			var N = det4(rvv.x, rvv.y, rvv.z, rvv.d, ru.x, ru.y, ru.z, ru.d, rv.x, rv.y, rv.z, rv.d, v00.x, v00.y, v00.z, v00.d);
			var M = det4(ruv.x, ruv.y, ruv.z, ruv.d, ru.x, ru.y, ru.z, ru.d, rv.x, rv.y, rv.z, rv.d, v00.x, v00.y, v00.z, v00.d);
			var E = (ru.x * v00.d - v00.x * ru.d) * (ru.x * v00.d - v00.x * ru.d) + (ru.y * v00.d - v00.y * ru.d) * (ru.y * v00.d - v00.y * ru.d) + (ru.z * v00.d - v00.z * ru.d) * (ru.z * v00.d - v00.z * ru.d);
			var G = (rv.x * v00.d - v00.x * rv.d) * (rv.x * v00.d - v00.x * rv.d) + (rv.y * v00.d - v00.y * rv.d) * (rv.y * v00.d - v00.y * rv.d) + (rv.z * v00.d - v00.z * rv.d) * (rv.z * v00.d - v00.z * rv.d);
			var F = (ru.x * v00.d - v00.x * ru.d) * (rv.x * v00.d - v00.x * rv.d) + (ru.y * v00.d - v00.y * ru.d) * (rv.y * v00.d - v00.y * rv.d) + (ru.z * v00.d - v00.z * ru.d) * (rv.z * v00.d - v00.z * rv.d);
			var kesv = new Vec3();
			kesv.x = det3(v00.y, v00.z, v00.d, ru.y, ru.z, ru.d, rv.y, rv.z, rv.d);
			kesv.y = det3(v00.x, v00.z, v00.d, ru.x, ru.z, ru.d, rv.x, rv.z, rv.d);
			kesv.z = det3(v00.x, v00.y, v00.d, ru.x, ru.y, ru.d, rv.x, rv.y, rv.d);
			var kes = kesv.dot(kesv);
			var crv_res = p.curvature[pi]; // pi input
			crv_res.gaussian = v00.d * v00.d * v00.d * v00.d * (L * N - M * M) / (kes * kes);
			crv_res.mean = -v00.d * (L * G - 2 * M * F + N * E) / Math.sqrt(kes * kes * kes) / 2;
			// TODO: why is the curvature sometimes NaN ?
			if (isNaN(crv_res.gaussian)) {{
				crv_res.gaussian = 0;
			}}
			if (isNaN(crv_res.mean)) {{
				crv_res.mean = 0;
			// JP23:  check kes < 0
			}}
			var disc = crv_res.mean * crv_res.mean - crv_res.gaussian;
			if (disc < 0) {{   // JP23: dubious
				crv_res.max = crv_res.mean;
				crv_res.min = crv_res.mean;
			}}
			else {{
				disc = Math.sqrt(disc);
				crv_res.max = crv_res.mean + disc;
				crv_res.min = crv_res.mean - disc;
			}}
		}}
		function evaluate_polyhedron(p) {{
			p.points = [];
			p.normals = [];
			p.curvature = [];
			for (var i = 0; i < p.mesh.length; ++i) {{
				p.points.push(p.mesh[i].dup());
				var n = new Vec3();
				p.normals.push(n);
				p.curvature.push({{ gaussian: 0, mean: 0, max: 0, min: 0 }});
			}}
			for (var i = 0; i < p.polyhedron_indices.length; i += 3) {{
				// compute normal of each triangle, average for each vertex
				var i0 = p.polyhedron_indices[i];
				var i1 = p.polyhedron_indices[i + 1];
				var i2 = p.polyhedron_indices[i + 2];
				var a = p.points[i0];
				var b = p.points[i1];
				var c = p.points[i2];
				// v0 = c - a
				var v0 = c.dup().sub(a);
				// v1 = b - a
				var v1 = b.dup().sub(a);
				// n = v0 cross v1
				var n = v0.dup().cross(v1).normalize();
				p.normals[i0].add(n);
				p.normals[i1].add(n);
				p.normals[i2].add(n);
			}}
			for (var i = 0; i < p.normals.length; ++i) {{
				p.normals[i].normalize();
			}}
		}}
		function evaluate_triangle(p, level) {{
			function b2i_i(i, j, k) {{
				var sum = j;
				for (var kk = 0; kk < k; ++kk) {{
					sum += p.degu + 1 - kk;
				}}
				return sum;
			}}
			function b2i_j(i, j, k) {{
				var sum = p.degu - i - k;
				for (var kk = 0; kk < k; ++kk) {{
					sum += p.degu + 1 - kk;
				}}
				return sum;
			}}
			function b2i_k(i, j, k) {{
				var sum = j;
				k = p.degu - i - j;
				for (var kk = 0; kk < k; ++kk) {{
					sum += p.degu + 1 - kk;
				}}
				return sum;
			}}
			var N = 1 << level;
			var size = Math.round((N + 1) * (N + 2) * 0.5);
			p.points = [];
			p.normals = [];
			p.curvature = [];
			for (var i = 0; i < size; ++i) {{
				p.points.push(new Vec3());
				p.normals.push(new Vec3());
				p.curvature.push({{ gaussian: 0, mean: 0, max: 0, min: 0 }});
			}}
			// buffer to be used later for de casteljau's algorithm
			var decastel = [];
			for (var i = 0; i < p.mesh.length; ++i) {{
				decastel.push(new Vec3());
			}}
			var pi = 0;
			for (var uu = 0; uu <= N; ++uu) {{
				for (var vv = 0; vv <= N - uu; ++vv) {{
					var on_boundary = uu == 0;
					var on_vertex = uu == 0 && vv == 0;
					// u,v,w are not integers
					var u = uu / N;
					var v = vv / N;
					var w = 1 - u - v;
					// different mapping functions are used for the interior and the boundary
					var b2i_1 = void 0;
					if (on_vertex) {{
						b2i_1 = b2i_k;
					}}
					else if (on_boundary) {{
						b2i_1 = b2i_j;
					}}
					else {{
						b2i_1 = b2i_i;
					}}
					// initalize buffer for DeCasteljau
					for (var i = 0; i <= p.degu; ++i) {{
						for (var j = 0; j <= p.degu - i; ++j) {{
							var k = p.degu - i - j;
							var index = b2i_1(i, j, k);
							decastel[index].copy(p.mesh[index]);
						}}
					}}
					// decasteljau algorithm
					for (var d = p.degu - 1; d >= 1; --d) {{
						for (var k = 0; k <= d; ++k) {{
							for (var j = 0; j <= d - k; ++j) {{
								var i = d - j - k;
								var dst = b2i_1(i, j, k);
								var srcu = b2i_1(i + 1, j, k);
								var srcv = b2i_1(i, j + 1, k);
								var srcw = b2i_1(i, j, k + 1);
								decastel[dst].x = u * decastel[srcu].x + v * decastel[srcv].x + w * decastel[srcw].x;
								decastel[dst].y = u * decastel[srcu].y + v * decastel[srcv].y + w * decastel[srcw].y;
								decastel[dst].z = u * decastel[srcu].z + v * decastel[srcv].z + w * decastel[srcw].z;
								decastel[dst].d = u * decastel[srcu].d + v * decastel[srcv].d + w * decastel[srcw].d;
							}}
						}}
					}}
					// last step of decasteljau
					var v00 = new Vec3();
					{{
						var srcu = b2i_1(1, 0, 0);
						var srcv = b2i_1(0, 1, 0);
						var srcw = b2i_1(0, 0, 1);
						v00.x = u * decastel[srcu].x + v * decastel[srcv].x + w * decastel[srcw].x;
						v00.y = u * decastel[srcu].y + v * decastel[srcv].y + w * decastel[srcw].y;
						v00.z = u * decastel[srcu].z + v * decastel[srcv].z + w * decastel[srcw].z;
					v00.d = u * decastel[srcu].d + v * decastel[srcv].d + w * decastel[srcw].d;
					}}
					var v01 = void 0;
					var v02 = void 0;
					var v10 = void 0;
					var v20 = void 0;
					var v11 = void 0;
					if (on_vertex) {{
						v01 = decastel[b2i_1(0, 1, 0)].dup();
						v10 = decastel[b2i_1(1, 0, 0)].dup();
						if (p.degu > 1) {{
							v02 = decastel[b2i_1(0, 2, 0)].dup();
							v20 = decastel[b2i_1(2, 0, 0)].dup();
							v11 = decastel[b2i_1(1, 1, 0)].dup();
						}}
					}}
					else if (on_boundary) {{
						v01 = decastel[b2i_1(1, 0, 0)].dup();
						v10 = decastel[b2i_1(0, 0, 1)].dup();
						if (p.degu > 1) {{
							v02 = decastel[b2i_1(2, 0, 0)].dup();
							v20 = decastel[b2i_1(0, 0, 2)].dup();
							v11 = decastel[b2i_1(1, 0, 1)].dup();
						}}
					}}
					else {{
						v01 = decastel[b2i_1(0, 0, 1)].dup();
						v10 = decastel[b2i_1(0, 1, 0)].dup();
						if (p.degu > 1) {{
							v02 = decastel[b2i_1(0, 0, 2)].dup();
							v20 = decastel[b2i_1(0, 2, 0)].dup();
							v11 = decastel[b2i_1(0, 1, 1)].dup();
						}}
					}}
					evaluate_at(p, pi, false, v00, v01, v02, v10, v20, v11);
					++pi;
				}}
			}}
			if (p.artificial_normals) {{
				function b2i(i, j, k) {{
					var sum = j;
					for (var kk = 0; kk < k; ++kk) {{
						sum += p.artificial_normals.degu + 1 - kk;
					}}
					return sum;
				}}
				var normal_index = 0;
				for (var uu = 0; uu <= N; ++uu) {{
					for (var vv = 0; vv <= N - uu; ++vv) {{
						// u,v,w are not integers
						var u = uu / N;
						var v = vv / N;
						var w = 1 - u - v;
						// initalize buffer for DeCasteljau
						for (var i = 0; i <= p.artificial_normals.degu; ++i) {{
							for (var j = 0; j <= p.artificial_normals.degu - i; ++j) {{
								var k = p.artificial_normals.degu - i - j;
								var index = b2i(i, j, k);
								decastel[index].copy(p.artificial_normals.normals[index]);
							}}
						}}
						// decasteljau algorithm
						for (var d = p.artificial_normals.degu - 1; d >= 0; --d) {{
							for (var k = 0; k <= d; ++k) {{
								for (var j = 0; j <= d - k; ++j) {{
									var i = d - j - k;
									var dst = b2i(i, j, k);
									var srcu = b2i(i + 1, j, k);
									var srcv = b2i(i, j + 1, k);
									var srcw = b2i(i, j, k + 1);
									decastel[dst].x = u * decastel[srcu].x + v * decastel[srcv].x + w * decastel[srcw].x;
									decastel[dst].y = u * decastel[srcu].y + v * decastel[srcv].y + w * decastel[srcw].y;
									decastel[dst].z = u * decastel[srcu].z + v * decastel[srcv].z + w * decastel[srcw].z;
						decastel[dst].d = u * decastel[srcu].d + v * decastel[srcv].d + w * decastel[srcw].d;
								}}
							}}
						}}
						p.normals[normal_index].copy(decastel[b2i(0, 0, 0)]).normalize();
						++normal_index;
					}}
				}}
			}}
		}}
		// one dimensional decasteljau
		function decastel_1(buffer, deg, u, out_p) {{
			for (var d = deg; d >= 1; --d) {{
				for (var i = 0; i < d; ++i) {{
					// buffer[i] = u*buffer[i] + (1 - u)*buffer[i + 1]
					// buffer[i] = buffer[i] + u*(buffer[i + 1] - buffer[i])
					// buffer[i] += (buffer[i + 1] - buffer[i])*u
					buffer[i].add(buffer[i + 1].dup().sub(buffer[i]).scale(u));
				}}
			}}
			out_p.copy(buffer[0]);
		}}
	</script>
	<script>
		var RenderablePatch = /** @class */ (function () {{
    function RenderablePatch(gl, patch) {{
        this.patch = patch;
        this.maxCrv = [0, 0, 0, 0];
        this.minCrv = [0, 0, 0, 0];
        this.boundingBoxMin = new Vec3();
        this.boundingBoxMax = new Vec3();
        this.positionBuffer = gl.createBuffer();
        this.normalBuffer = gl.createBuffer();
        this.visualNormalBuffer = gl.createBuffer();

        // to display curvature colors on the visual normal
        this.duplacatedPointsBuffer = gl.createBuffer();
        this.duplicatedNormalsBuffer = gl.createBuffer();
        this.duplicatedCurvatureBuffer = gl.createBuffer();
        this.visualNormalVertexIdBuffer = gl.createBuffer();
        this.visualNormalBufferLength = 0;

        this.indexBuffer = gl.createBuffer();
        this.indexBufferLength = 0;
        this.curvatureBuffer = gl.createBuffer();
        this.controlMesh = {{
            positionBuffer: gl.createBuffer(),
            indexBuffer: gl.createBuffer(),
            indexBufferLength: 0
        }};
    }}
    RenderablePatch.prototype.evaluate = function (gl, level) {{
        switch (this.patch.kind) {{
            case PatchType.Triangle:
                evaluate_triangle(this.patch, level);
                break;
            case PatchType.Quadrilateral:
                evaluate_quad(this.patch, level);
                break;
            default:
                evaluate_polyhedron(this.patch);
        }}
        this.fill_pnc_buffer(gl);
        this.fill_visual_normal_buffer(gl);
        switch (this.patch.kind) {{
            case PatchType.Triangle:
                this.fill_index_buffer_tri(gl, level);
                break;
            case PatchType.Quadrilateral:
                this.fill_index_buffer_quad(gl, level);
                break;
            default:
                this.fill_index_buffer_poly(gl);
        }}
        this.findMinMax();
        
    }};
    // fill the buffer for the visual normals
    RenderablePatch.prototype.fill_visual_normal_buffer = function (gl) {{
        var N = this.patch.points.length;
        var duplicatedPointsArr = new Float32Array(N * 8);
        var duplicatedNormalsArr = new Float32Array(N * 6);
        var duplicatedCurvatureArr = new Float32Array(N * 8);
        var visualNormalVertexIdArr = new Float32Array(N * 2);
        for (var i = 0; i < N; ++i) {{
            this.patch.normals[i].normalize();
            duplicatedPointsArr[i * 8] = this.patch.points[i].x;
            duplicatedPointsArr[i * 8 + 1] = this.patch.points[i].y;
            duplicatedPointsArr[i * 8 + 2] = this.patch.points[i].z;
            duplicatedPointsArr[i * 8 + 3] = 1.0;
            duplicatedPointsArr[i * 8 + 4] = this.patch.points[i].x;
            duplicatedPointsArr[i * 8 + 5] = this.patch.points[i].y;
            duplicatedPointsArr[i * 8 + 6] = this.patch.points[i].z;
            duplicatedPointsArr[i * 8 + 7] = 1.0;

            // storing curvature for each vertex in the visual normal

            duplicatedCurvatureArr[i * 8] = this.patch.curvature[i].gaussian;
            duplicatedCurvatureArr[i * 8 + 1] = this.patch.curvature[i].mean;
            duplicatedCurvatureArr[i * 8 + 2] = this.patch.curvature[i].max;
            duplicatedCurvatureArr[i * 8 + 3] = this.patch.curvature[i].min;
            duplicatedCurvatureArr[i * 8 + 4] = this.patch.curvature[i].gaussian;
            duplicatedCurvatureArr[i * 8 + 5] = this.patch.curvature[i].mean;
            duplicatedCurvatureArr[i * 8 + 6] = this.patch.curvature[i].max;
            duplicatedCurvatureArr[i * 8 + 7] = this.patch.curvature[i].min;

            duplicatedNormalsArr[i * 6] = this.patch.normals[i].x;
            duplicatedNormalsArr[i * 6 + 1] = this.patch.normals[i].y;
            duplicatedNormalsArr[i * 6 + 2] = this.patch.normals[i].z;
            duplicatedNormalsArr[i * 6 + 3] = this.patch.normals[i].x;
            duplicatedNormalsArr[i * 6 + 4] = this.patch.normals[i].y;
            duplicatedNormalsArr[i * 6 + 5] = this.patch.normals[i].z;

            visualNormalVertexIdArr[i * 2] = 0.0;
            visualNormalVertexIdArr[i * 2 + 1] = 1.0;
        }}
        gl.bindBuffer(gl.ARRAY_BUFFER, this.duplacatedPointsBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, duplicatedPointsArr, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ARRAY_BUFFER, this.duplicatedNormalsBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, duplicatedNormalsArr, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ARRAY_BUFFER, this.duplicatedCurvatureBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, duplicatedCurvatureArr, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ARRAY_BUFFER, this.visualNormalVertexIdBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, visualNormalVertexIdArr, gl.STATIC_DRAW);
        this.visualNormalBufferLength = N*2;
    }}
    // fill the buffer for the points, normals, and curvature
    RenderablePatch.prototype.fill_pnc_buffer = function (gl) {{
        if (this.patch.points.length != this.patch.curvature.length || this.patch.points.length != this.patch.normals.length) {{
            throw 'in fill_pnc_buffer: number of normals, curvature values, and points are not the same';
        }}
        var N = this.patch.points.length;
        var positionArr = new Float32Array(N * 4);
        for (var i = 0; i < N; ++i) {{
            positionArr[i * 4] = this.patch.points[i].x;
            positionArr[i * 4 + 1] = this.patch.points[i].y;
            positionArr[i * 4 + 2] = this.patch.points[i].z;
            positionArr[i * 4 + 3] = 1.0;
        }}
        var normalArr = new Float32Array(N * 3);
        for (var i = 0; i < N; ++i) {{
            normalArr[i * 3] = this.patch.normals[i].x;
            normalArr[i * 3 + 1] = this.patch.normals[i].y;
            normalArr[i * 3 + 2] = this.patch.normals[i].z;
        }}
        var curvatureArr = new Float32Array(N * 4);
        for (var i = 0; i < N; ++i) {{
            curvatureArr[i * 4] = this.patch.curvature[i].gaussian;
            curvatureArr[i * 4 + 1] = this.patch.curvature[i].mean;
            curvatureArr[i * 4 + 2] = this.patch.curvature[i].max;
            curvatureArr[i * 4 + 3] = this.patch.curvature[i].min;
        }}
        var cmPositionArr = new Float32Array(this.patch.mesh.length * 4);
        for (var i = 0; i < this.patch.mesh.length; ++i) {{
            cmPositionArr[i * 4] = this.patch.mesh[i].x;
            cmPositionArr[i * 4 + 1] = this.patch.mesh[i].y;
            cmPositionArr[i * 4 + 2] = this.patch.mesh[i].z;
            cmPositionArr[i * 4 + 3] = this.patch.mesh[i].d;
        }}
        gl.bindBuffer(gl.ARRAY_BUFFER, this.positionBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, positionArr, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ARRAY_BUFFER, this.normalBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, normalArr, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ARRAY_BUFFER, this.curvatureBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, curvatureArr, gl.STATIC_DRAW);
        gl.bindBuffer(gl.ARRAY_BUFFER, this.controlMesh.positionBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, cmPositionArr, gl.STATIC_DRAW);
    }};
    RenderablePatch.prototype.fill_index_buffer_quad = function (gl, level) {{
        var N = 1 << level;
        this.indexBufferLength = N * N * 6;
        var indexArr = new Uint32Array(this.indexBufferLength);
        for (var i = 0, dst = 0; i < N; ++i) {{
            // pretend like the single call to triangles is actually multiple triangle strips
            // use the "previous" vertices in the new triangle
            var v0 = i * (N + 1);
            var v1 = (i + 1) * (N + 1);
            for (var j = 1; j <= N; ++j) {{
                var v2 = i * (N + 1) + j;
                var v3 = (i + 1) * (N + 1) + j;
                indexArr[dst++] = v0;
                indexArr[dst++] = v1;
                indexArr[dst++] = v2;
                indexArr[dst++] = v1;
                indexArr[dst++] = v2;
                indexArr[dst++] = v3;
                v0 = v2;
                v1 = v3;
            }}
        }}
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.indexBuffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indexArr, gl.STATIC_DRAW);
        // fill the buffer for the control mesh
        var degu = this.patch.degu;
        var degv = this.patch.degv;
        this.controlMesh.indexBufferLength = degu * degv * 8;
        var cmIndexArr = new Uint32Array(this.controlMesh.indexBufferLength);
        for (var i = 0, dst = 0; i < degu; ++i) {{
            for (var j = 0; j < degv; ++j) {{
                var v0 = i * (degv + 1) + j;
                var v1 = (i + 1) * (degv + 1) + j;
                var v2 = (i + 1) * (degv + 1) + j + 1;
                var v3 = i * (degv + 1) + j + 1;
                cmIndexArr[dst++] = v0;
                cmIndexArr[dst++] = v1;
                cmIndexArr[dst++] = v1;
                cmIndexArr[dst++] = v2;
                cmIndexArr[dst++] = v2;
                cmIndexArr[dst++] = v3;
                cmIndexArr[dst++] = v3;
                cmIndexArr[dst++] = v0;
            }}
        }}
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.controlMesh.indexBuffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, cmIndexArr, gl.STATIC_DRAW);
    }};
    RenderablePatch.prototype.fill_index_buffer_poly = function (gl) {{
        this.indexBufferLength = this.patch.polyhedron_indices.length;
        var indexArr = new Uint32Array(this.patch.polyhedron_indices);
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.indexBuffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indexArr, gl.STATIC_DRAW);
        this.controlMesh.indexBufferLength = this.patch.polyhedron_edges.length;
        var cmIndexArr = new Uint32Array(this.patch.polyhedron_edges);
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.controlMesh.indexBuffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, cmIndexArr, gl.STATIC_DRAW);
    }};
    RenderablePatch.prototype.fill_index_buffer_tri = function (gl, level) {{
        function b2i_i(i, j, k, d) {{
            var sum = j;
            for (var kk = 0; kk < k; ++kk) {{
                sum += d + 1 - kk;
            }}
            return sum;
        }}
        var N = 1 << level;
        // this.indexBufferLength = N*(N/2)*6;
        this.indexBufferLength = N * N * 3;
        var indexArr = new Uint32Array(this.indexBufferLength);
        for (var i = 0, dst = 0; i < N; ++i) {{
            // pretend like the single call to triangles is actually multiple triangle strips
            // use the "previous" vertices in the new triangle
            var v0 = b2i_i(i + 1, 0, N - i - 1, N);
            var v1 = b2i_i(i, 0, N - i, N);
            for (var j = 1; j < N - i; ++j) {{
                var v2 = b2i_i(i + 1, j, N - i - j - 1, N);
                var v3 = b2i_i(i, j, N - i - j, N);
                indexArr[dst++] = v0;
                indexArr[dst++] = v1;
                indexArr[dst++] = v2;
                indexArr[dst++] = v1;
                indexArr[dst++] = v2;
                indexArr[dst++] = v3;
                v0 = v2;
                v1 = v3;
            }}
            indexArr[dst++] = v0;
            indexArr[dst++] = v1;
            indexArr[dst++] = b2i_i(i, N - i, 0, N);
        }}
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.indexBuffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indexArr, gl.STATIC_DRAW);
        // fill the buffer for the control mesh
        var deg = this.patch.degu;
        var d = this.patch.degu - 1;
        // this.controlMesh.indexBufferLength = (deg*(deg + 1)/2)*6;
        this.controlMesh.indexBufferLength = deg * (deg + 1) * 3;
        var cmIndexArr = new Uint32Array(this.controlMesh.indexBufferLength);
        for (var i = 0, dst = 0; i <= d; ++i) {{
            for (var j = 0; j <= d - i; ++j) {{
                var k = d - i - j;
                var v0 = b2i_i(i + 1, j, k, deg);
                var v1 = b2i_i(i, j + 1, k, deg);
                var v2 = b2i_i(i, j, k + 1, deg);
                cmIndexArr[dst++] = v0;
                cmIndexArr[dst++] = v1;
                cmIndexArr[dst++] = v1;
                cmIndexArr[dst++] = v2;
                cmIndexArr[dst++] = v2;
                cmIndexArr[dst++] = v0;
            }}
        }}
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.controlMesh.indexBuffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, cmIndexArr, gl.STATIC_DRAW);
    }};
    // finds the minimum and maximum position and curvature values
    // position used for bounding box
    // curvature used for color coding
    // (this is for one patch)
    RenderablePatch.prototype.findMinMax = function () {{
        if (this.patch.points.length == 0) {{
            this.boundingBoxMin.set(0.5, 0.5, 0.5);
            this.boundingBoxMax.set(-0.5, -0.5, -0.5);
            for (var k = 0; k < 4; ++k) {{
                this.minCrv[k] = 0;
                this.maxCrv[k] = 0;
            }}
            return;
        }}
        this.boundingBoxMin.copy(this.patch.points[0]);
        this.boundingBoxMax.copy(this.patch.points[0]);
        this.minCrv[0] = this.patch.curvature[0].gaussian;
        this.minCrv[1] = this.patch.curvature[0].mean;
        this.minCrv[2] = this.patch.curvature[0].max;
        this.minCrv[3] = this.patch.curvature[0].min;
        this.maxCrv[0] = this.patch.curvature[0].gaussian;
        this.maxCrv[1] = this.patch.curvature[0].mean;
        this.maxCrv[2] = this.patch.curvature[0].max;
        this.maxCrv[3] = this.patch.curvature[0].min;
        for (var i = 0; i < this.patch.points.length; ++i) {{
            var p = this.patch.points[i];
            this.boundingBoxMin.x = Math.min(p.x, this.boundingBoxMin.x);
            this.boundingBoxMin.y = Math.min(p.y, this.boundingBoxMin.y);
            this.boundingBoxMin.z = Math.min(p.z, this.boundingBoxMin.z);
            this.boundingBoxMax.x = Math.max(p.x, this.boundingBoxMax.x);
            this.boundingBoxMax.y = Math.max(p.y, this.boundingBoxMax.y);
            this.boundingBoxMax.z = Math.max(p.z, this.boundingBoxMax.z);
            var crv = this.patch.curvature[i];
            this.minCrv[0] = Math.min(crv.gaussian, this.minCrv[0]);
            this.minCrv[1] = Math.min(crv.mean, this.minCrv[1]);
            this.minCrv[2] = Math.min(crv.max, this.minCrv[2]);
            this.minCrv[3] = Math.min(crv.min, this.minCrv[3]);
            this.maxCrv[0] = Math.max(crv.gaussian, this.maxCrv[0]);
            this.maxCrv[1] = Math.max(crv.mean, this.maxCrv[1]);
            this.maxCrv[2] = Math.max(crv.max, this.maxCrv[2]);
            this.maxCrv[3] = Math.max(crv.min, this.maxCrv[3]);
        }}
    }};
    RenderablePatch.prototype.free = function (gl) {{
        gl.deleteBuffer(this.positionBuffer);
        gl.deleteBuffer(this.normalBuffer);
        gl.deleteBuffer(this.duplacatedPointsBuffer);
        gl.deleteBuffer(this.duplicatedNormalsBuffer);
        gl.deleteBuffer(this.duplicatedCurvatureBuffer);
        gl.deleteBuffer(this.visualNormalVertexIdBuffer);
        gl.deleteBuffer(this.indexBuffer);
        gl.deleteBuffer(this.curvatureBuffer);
        gl.deleteBuffer(this.controlMesh.positionBuffer);
        gl.deleteBuffer(this.indexBuffer);
        this.indexBufferLength = 0;
        this.visualNormalBufferLength = 0;
    }};
    return RenderablePatch;
}}());
var Group = /** @class */ (function () {{
    function Group(name, id, useDefaults) {{
        this.name = name;
        this.id = id;
        this.objs = [];
        this.maxCrv = [0, 0, 0, 0];
        this.minCrv = [0, 0, 0, 0];
        this.boundingBoxMin = new Vec3();
        this.boundingBoxMax = new Vec3();
        this.color = 0;
        if (useDefaults || !renderState.globalGroup) {{
            this.highlightDensity = 0.5;
            this.highlightResolution = 10;
            this.visualNormalSize = 1.0;
            this.flatShading = false;
            this.flipNormals = false;
            this.showControlMesh = false;
            this.showPatches = true;
            this.showVisualNormals = false;
            this.highlight = Highlight.Normal;
        }}
        else {{
            this.highlightDensity = renderState.globalGroup.highlightDensity;
            this.highlightResolution = renderState.globalGroup.highlightResolution;
            this.visualNormalSize = renderState.globalGroup.visualNormalSize;
            this.flatShading = renderState.globalGroup.flatShading;
            this.flipNormals = renderState.globalGroup.flipNormals;
            this.showControlMesh = renderState.globalGroup.showControlMesh;
            this.showPatches = renderState.globalGroup.showPatches;
            this.showVisualNormals = renderState.globalGroup.showVisualNormals;
            this.highlight = renderState.globalGroup.highlight;
        }}
    }}
    // finds the minimum and maximum position and curvature values
    // position used for bounding box
    // curvature used for color coding
    // (this is for the entire group and should be done only after all objects are evaluated)
    Group.prototype.findMinMax = function () {{
        if (this.objs.length == 0) {{
            this.boundingBoxMin.set(0.5, 0.5, 0.5);
            this.boundingBoxMax.set(-0.5, -0.5, -0.5);
            for (var k = 0; k < 4; ++k) {{
                this.minCrv[k] = 0;
                this.maxCrv[k] = 0;
            }}
            return;
        }}
        this.boundingBoxMin.copy(this.objs[0].boundingBoxMin);
        this.boundingBoxMax.copy(this.objs[0].boundingBoxMax);
        for (var k = 0; k < 4; ++k) {{
            this.minCrv[k] = this.objs[0].minCrv[k];
            this.maxCrv[k] = this.objs[0].maxCrv[k];
        }}
        for (var i = 1; i < this.objs.length; ++i) {{
            var obj = this.objs[i];
            this.boundingBoxMin.x = Math.min(obj.boundingBoxMin.x, this.boundingBoxMin.x);
            this.boundingBoxMin.y = Math.min(obj.boundingBoxMin.y, this.boundingBoxMin.y);
            this.boundingBoxMin.z = Math.min(obj.boundingBoxMin.z, this.boundingBoxMin.z);
            this.boundingBoxMax.x = Math.max(obj.boundingBoxMax.x, this.boundingBoxMax.x);
            this.boundingBoxMax.y = Math.max(obj.boundingBoxMax.y, this.boundingBoxMax.y);
            this.boundingBoxMax.z = Math.max(obj.boundingBoxMax.z, this.boundingBoxMax.z);
            for (var k = 0; k < 4; ++k) {{
                this.minCrv[k] = Math.min(obj.minCrv[k], this.minCrv[k]);
                this.maxCrv[k] = Math.max(obj.maxCrv[k], this.maxCrv[k]);
            }}
        }}
    }};
    Group.prototype.free = function (gl) {{
        for (var i = 0; i < this.objs.length; ++i) {{
            this.objs[i].free(gl);
        }}
    }};
    return Group;
}}());
// parses the text for patches
function readBVFile(gl, text) {{
    var input = text.split(/\\s+/);
    var cur = 0;
    function read_vector(n, isRational) {{
        var arr = [];
        for (var i = 0; i < n; ++i) {{
            var v = new Vec3();
            v.x = Number(input[cur]);
            ++cur;
            v.y = Number(input[cur]);
            ++cur;
            v.z = Number(input[cur]);
            ++cur;
            if (isRational) {{
                v.d = Number(input[cur]);
                ++cur;
            }}
            arr.push(v);
        }}
        return arr;
    }}
    var groups = [];
    var currentGroup = new Group('(unamed group)', 0, false);
    while (cur < input.length && input[cur] != '') {{
        if (input[cur].toUpperCase() == "GROUP") {{
            var id = Number(input[++cur]);
            var name_1 = input[++cur];
            var groupExists = false;
            for (var i = 0; i < groups.length; ++i) {{
                if (groups[i].id == id) {{
                    currentGroup = groups[i];
                    groupExists = true;
                    break;
                }}
            }}
            if (!groupExists) {{
                currentGroup = new Group(name_1, id, false);
                groups.push(currentGroup);
            }}
            ++cur;
        }}
        var kind = Number(input[cur]);
        ++cur;
        switch (kind) {{
            case 1: {{
                // polyhedral data (vertex + faces)
                var numVertices = Number(input[cur]);
                cur += 1;
                var numFaces = Number(input[cur]);
                cur += 1;
                // load vertices
                var vertices = [];
                for (var i = 0; i < numVertices; i++) {{
                    var x = Number(input[cur + 0]);
                    var y = Number(input[cur + 1]);
                    var z = Number(input[cur + 2]);
                    var v = new Vec3();
                    v.set(x, y, z);
                    vertices.push(v);
                    cur += 3;
                }}
                // load faces
                var faces = [];
                var edges = []
                for (var i = 0; i < numFaces; i++) {{
                    var faceSize = Number(input[cur]);
                    cur += 1;
                    var verts = [];
                        for (var j = 0; j < faceSize; j++) {{
                            verts.push(Number(input[cur++]));
                        }}
                        for (var j = 0; j < faceSize-2; j++) {{
                            faces.push(verts[0]);
                            faces.push(verts[j+1]);
                            faces.push(verts[j+2]);
                        }}
                        for (var j = 0; j < faceSize; j++) {{
                            edges.push(verts[j]);
                            edges.push(verts[(j+1)%faceSize]);
                        }}
                    
                }}
                var p = Patch.MakePolyhedral(vertices, faces, edges);
                currentGroup.objs.push(new RenderablePatch(gl, p));
                break;
            }}
            case 3:
            case 11: {{
                // triangular bezier patch
                var isRational = kind == 11;
                var deg = Number(input[cur]);
                ++cur;
                var cp = read_vector(((deg + 2) * (deg + 1)) / 2, isRational);
                var p = Patch.MakeTriangle(deg, cp);
                currentGroup.objs.push(new RenderablePatch(gl, p));
                break;
            }}
            case 4:
            case 5:
            case 8: {{
                // square quad patch (4), general quad patch (5) or rational patch (8)
                var isSquare = kind == 4;
                var isRational = kind == 8;
                var degu = Number(input[cur++]);
                var degv = isSquare ? degu : Number(input[cur++]);
                var cp = read_vector((degu + 1) * (degv + 1), isRational);
                var p = Patch.MakeQuad(degu, degv, cp);
                currentGroup.objs.push(new RenderablePatch(gl, p));
                break;
            }}
            case 6: {{
                // Trim curve
                throw 'Trim curve (6) not supported';
            }}
            case 7: {{
                // B-spline tensor product
                throw 'B-spline (7) not supported';
            }}
            case 9: {{
                // PN triangle
                var deg = Number(input[cur++]);
                var normal_deg = Number(input[cur++]);
                var cp = read_vector(((deg + 2) * (deg + 1)) / 2, false);
                var normals = read_vector(((normal_deg + 2) * (normal_deg + 1)) / 2, false);
                var p = Patch.MakeTriangle(deg, cp);
                p.artificial_normals = {{
                    degu: normal_deg,
                    degv: normal_deg,
                    normals: normals
                }};
                currentGroup.objs.push(new RenderablePatch(gl, p));
                break;
            }}
            case 10: {{
                // PN quad
                var degu = Number(input[cur++]);
                var degv = Number(input[cur++]);
                var normal_degu = Number(input[cur++]);
                var normal_degv = Number(input[cur++]);
                var cp = read_vector((degu + 1) * (degv + 1), false);
                var normals = read_vector((normal_degu + 1) * (normal_degv + 1), false);
                var p = Patch.MakeQuad(degu, degv, cp);
                p.artificial_normals = {{
                    degu: normal_degu,
                    degv: normal_degv,
                    normals: normals
                }};
                currentGroup.objs.push(new RenderablePatch(gl, p));
                break;
            }}
            default:
                throw 'kind not supported: ' + kind.toString();
        }}
    }}
    // if no groups were specified, use the default (named) group
    if (groups.length == 0) {{
        groups.push(currentGroup);
    }}
    for (var i = 0; i < groups.length; ++i) {{
        groups[i].color = i % GroupColors.length;
    }}
    return groups;
}}

	</script>
	<script>
		/* important: all matrices are given in column ordering,
so a matrix is stored with it's array indices as follows:
0   4   8   12
1   5   9   13
2   6   10  14
3   7   11  15
*/
var Mat4 = /** @class */ (function () {{
    function Mat4() {{
        this.m = new Float32Array(16);
        // initalize as identity
        this.m[0] = 1;
        this.m[5] = 1;
        this.m[10] = 1;
        this.m[15] = 1;
    }}
    Mat4.prototype.copy = function (other) {{
        for (var i = 0; i < 16; ++i) {{
            this.m[i] = other.m[i];
        }}
        return this;
    }};
    Mat4.prototype.dup = function () {{
        var other = new Mat4();
        for (var i = 0; i < 16; ++i) {{
            other.m[i] = this.m[i];
        }}
        return other;
    }};
    Mat4.prototype.setIdentity = function () {{
        for (var i = 0; i < 4; i++) {{
            for (var j = 0; j < 4; j++) {{
                this.m[i * 4 + j] = i == j ? 1.0 : 0.0;
            }}
        }}
    }};
    Mat4.prototype.mul = function (other) {{
        var buf = new Float32Array(16);
        for (var i = 0; i < 4; ++i) {{
            for (var j = 0; j < 4; ++j) {{
                for (var k = 0; k < 4; ++k) {{
                    buf[j * 4 + i] += this.m[k * 4 + i] * other.m[j * 4 + k];
                }}
            }}
        }}
        this.m = buf;
    }};
    Mat4.prototype.toString = function () {{
        var ret = this.m[0] + ' ' + this.m[4] + ' ' + this.m[8] + ' ' + this.m[12] + '\\n';
        ret += this.m[1] + ' ' + this.m[5] + ' ' + this.m[9] + ' ' + this.m[13] + '\\n';
        ret += this.m[2] + ' ' + this.m[6] + ' ' + this.m[10] + ' ' + this.m[14] + '\\n';
        ret += this.m[3] + ' ' + this.m[7] + ' ' + this.m[11] + ' ' + this.m[15] + '\\n';
        return ret;
    }};
    Mat4.makeCopy = function (other) {{
        var ret = new Mat4();
        ret.copy(other);
        return ret;
    }};
    Mat4.makeScale = function (x, y, z) {{
        var ret = new Mat4();
        ret.m[0] = x;
        ret.m[5] = y;
        ret.m[10] = z;
        return ret;
    }};
    Mat4.makeTranslation = function (x, y, z) {{
        var ret = new Mat4();
        ret.m[12] = x;
        ret.m[13] = y;
        ret.m[14] = z;
        return ret;
    }};
    Mat4.makeQuaternion = function (q) {{
        var ret = new Mat4();
        ret.m[0] = 1 - 2 * q.y * q.y - 2 * q.z * q.z;
        ret.m[4] = 2 * q.x * q.y - 2 * q.z * q.d;
        ret.m[8] = 2 * q.x * q.z + 2 * q.y * q.d;
        ret.m[1] = 2 * q.x * q.y + 2 * q.z * q.d;
        ret.m[5] = 1 - 2 * q.x * q.x - 2 * q.z * q.z;
        ret.m[9] = 2 * q.y * q.z - 2 * q.x * q.d;
        ret.m[2] = 2 * q.x * q.z - 2 * q.y * q.d;
        ret.m[6] = 2 * q.y * q.z + 2 * q.x * q.d;
        ret.m[10] = 1 - 2 * q.x * q.x - 2 * q.y * q.y;
        return ret;
    }};
    return Mat4;
}}());

	</script>
	<script>
		var GroupColors = [
    {{ name: 'Yellow', value: [0.7, 0.7, 0.1, 1.0] }},
    {{ name: 'Green', value: [0.1, 0.7, 0.1, 1.0] }},
    {{ name: 'Silver', value: [0.75, 0.75, 0.75, 1.0] }},
    {{ name: 'Red', value: [0.7, 0.1, 0.1, 1.0] }},
    {{ name: 'Cyan', value: [0.1, 0.7, 0.7, 1.0] }},
    {{ name: 'Magenta', value: [0.7, 0.1, 0.7, 1.0] }},
    {{ name: 'Orange', value: [0.7, 0.4, 0.1, 1.0] }},
    {{ name: 'Purple', value: [0.4, 0.1, 0.4, 1.0] }},
    {{ name: 'Blue', value: [0.1, 0.1, 0.7, 1.0] }},
];
var Highlight;
(function (Highlight) {{
    Highlight[Highlight["Normal"] = 0] = "Normal";
    Highlight[Highlight["Line"] = 1] = "Line";
    Highlight[Highlight["Refelection"] = 2] = "Refelection";
    Highlight[Highlight["Curvature"] = 3] = "Curvature";
    Highlight[Highlight["Wireframe"] = 4] = "Wireframe";
}})(Highlight || (Highlight = {{}}));
var CurvatureType;
(function (CurvatureType) {{
    CurvatureType[CurvatureType["Gaussian"] = 0] = "Gaussian";
    CurvatureType[CurvatureType["Mean"] = 1] = "Mean";
    CurvatureType[CurvatureType["Max"] = 2] = "Max";
    CurvatureType[CurvatureType["Min"] = 3] = "Min";
}})(CurvatureType || (CurvatureType = {{}}));
var defaultSettings = {{
    tessellation: 2,
    showBoundingBox: false,
    showWatermark: true,
    lightsOn: [1.0, 0.0, 0.0],
    userMaxCrv: 0,
    userMinCrv: 0,
    curvatureType: CurvatureType.Gaussian
}};
var settings = defaultSettings;
// Active state of the renderer, we use it instead of an object with methods
var renderState = {{
    groups: [],
    // this group represents when a shader setting is applied to all groups
    globalGroup: new Group("All Groups", -1, true),
    selectedGroupIndex: -1,
    projection: new Mat4(),
    aspectRatio: 1.0,
    translation: new Float32Array([0, 0, 0]),
    origin: new Float32Array([0, 0, 0]),
    // rotation is a quaternion
    rotation: new Vec3(),
    rotateMode: true,
    scale: 1.0,
    zoom: 0.8264462809917354,
    modelview: new Mat4(),
    clipping: -55.0,
    context: null,
    highlightShader: null,
    curvatureShader: null,
    reflectionShader: null,
    shader: null,
    boundingBoxMin: new Vec3(),
    boundingBoxMax: new Vec3(),
    transparency: 1.0
}};
;
var savedPositions = [];
function loadTextResource(url, cb) {{
    var x = new XMLHttpRequest();
    x.addEventListener('load', function (e) {{
        cb(false, x.responseText);
    }});
    x.addEventListener('error', function (e) {{
        console.log('Error loading resource ' + url);
        cb(true, '');
    }});
    x.open('GET', url, true);
    x.responseType = 'text';
    x.send();
}}
function makeShader(gl, type, src) {{
    var s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (gl.getShaderParameter(s, gl.COMPILE_STATUS) === false) {{
        throw "Shader error: " + (gl.getShaderInfoLog(s));
    }}
    else {{
        return s;
    }}
}}
function makeProgram(gl, vs, fs) {{
    var p = gl.createProgram();
    gl.attachShader(p, vs);
    gl.attachShader(p, fs);
    gl.linkProgram(p);
    if (gl.getProgramParameter(p, gl.LINK_STATUS) === false) {{
        throw "Program link error: " + (gl.getProgramInfoLog(p));
    }}
    else {{
        return p;
    }}
}}
function updateProjection() {{
    var gl = renderState.context;
    gl.viewport(0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight);
    renderState.projection.setIdentity();
    renderState.projection.mul(Mat4.makeScale(renderState.zoom, renderState.zoom * gl.drawingBufferWidth / gl.drawingBufferHeight, 1));
    // diagonal = || boxMax - boxMin ||
    var diagonal = renderState.boundingBoxMax.dup().sub(renderState.boundingBoxMin).length();
    renderState.scale = 1 / diagonal;
    // middle = ( boxMax + boxMin ) / 2
    var middle = renderState.boundingBoxMax.dup().add(renderState.boundingBoxMin).scale(0.5);
    renderState.origin[0] = middle.x;
    renderState.origin[1] = middle.y;
    renderState.origin[2] = middle.z;
}}
function updateModelView() {{
    var mv = renderState.modelview;
    var o = renderState.origin;
    var r = renderState.rotation;
    var s = renderState.scale;
    var trs = renderState.translation;
    mv.setIdentity();
    mv.mul(Mat4.makeTranslation(trs[0], trs[1], trs[2]));
    mv.mul(Mat4.makeScale(s, s, s));
    mv.mul(Mat4.makeQuaternion(r));
    mv.mul(Mat4.makeTranslation(-o[0], -o[1], -o[2]));
}}
var wireCubeArrayBuffer;
var wireCubeIndexBuffer;
function draw(timestamp) {{
    var gl = renderState.context;
    gl.clear(gl.COLOR_BUFFER_BIT + gl.DEPTH_BUFFER_BIT);
    for (var i = 0; i < renderState.groups.length; ++i) {{
        drawGroup(renderState.groups[i]);
    }}
    if (settings.showBoundingBox) {{
        // scale = max - min
        var boxScale = renderState.boundingBoxMax.dup().sub(renderState.boundingBoxMin);
        var r = renderState.rotation;
        var s = renderState.scale;
        var trs = renderState.translation;
        var mv = new Mat4();
        mv.mul(Mat4.makeTranslation(trs[0], trs[1], trs[2]));
        mv.mul(Mat4.makeScale(s, s, s));
        mv.mul(Mat4.makeQuaternion(r));
        mv.mul(Mat4.makeScale(boxScale.x, boxScale.y, boxScale.z));
        gl.useProgram(renderState.shader.program);
        gl.disableVertexAttribArray(renderState.shader.attrNormal);
        // make the bounding box black
        gl.uniform4fv(renderState.shader.uniDiffuse, [0, 0, 0, 1]);
        gl.uniformMatrix4fv(renderState.shader.uniModelView, false, mv.m);
        gl.uniformMatrix4fv(renderState.shader.uniProjection, false, renderState.projection.m);
        gl.bindBuffer(gl.ARRAY_BUFFER, wireCubeArrayBuffer);
        gl.vertexAttribPointer(renderState.shader.attrPosition, 4, gl.FLOAT, false, 0, 0);
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, wireCubeIndexBuffer);
        gl.drawElements(gl.LINES, 24, gl.UNSIGNED_INT, 0);
        gl.enableVertexAttribArray(renderState.shader.attrNormal);
    }}
    window.requestAnimationFrame(draw);
}}
function drawGroup(group) {{
    var gl = renderState.context;
    var shader;
    switch (group.highlight) {{
        case Highlight.Line:
            shader = renderState.highlightShader;
            break;
        case Highlight.Refelection:
            shader = renderState.reflectionShader;
            break;
        case Highlight.Curvature:
            shader = renderState.curvatureShader;
            break;
        default:
            shader = renderState.shader;
    }}
    gl.useProgram(shader.program);
    gl.uniformMatrix4fv(shader.uniProjection, false, renderState.projection.m);
    gl.uniformMatrix4fv(shader.uniModelView, false, renderState.modelview.m);
    gl.uniform1f(shader.uniClipAmt, renderState.clipping);
    if (group.highlight === Highlight.Curvature) {{
        // only things for curvature shaders
        var crvShader = shader;
        gl.enableVertexAttribArray(crvShader.attrCurvature);
        gl.uniform1f(crvShader.uniMaxCrv, settings.userMaxCrv);
        gl.uniform1f(crvShader.uniMinCrv, settings.userMinCrv);
        gl.uniform1i(crvShader.uniCrvMode, settings.curvatureType);
    }}
    else {{
        // only things for ordinary shaders and highlight line / reflection shaders
        var s = shader;
        gl.enableVertexAttribArray(s.attrNormal);
        gl.uniform1i(s.uniFlipNormals, group.flipNormals ? 1.0 : 0.0);
        gl.uniform3fv(s.uniLightsOn, settings.lightsOn);
    }}
    gl.enableVertexAttribArray(shader.attrPosition);
    if (group.highlight == Highlight.Line || group.highlight == Highlight.Refelection) {{
        // things for highlight line / reflection shaders only
        var s = shader;
        gl.uniform1f(s.uniHighLightDensity, group.highlightDensity);
        gl.uniform1f(s.uniHighlightResolution, group.highlightResolution);
    }}
    else if (group.highlight == Highlight.Normal) {{
        // things for orinary shader only
        var s = shader;
        gl.uniform1i(s.uniFlatShading, group.flatShading ? 1.0 : 0.0);
    }}
    // all patch rendering
    if (group.showPatches) {{
        for (var j = 0; j < group.objs.length; ++j) {{
            var obj = group.objs[j];
            var color = GroupColors[group.color].value;
            // set the alpha to the current transparency
            color[3] = renderState.transparency;
            if (group.highlight === Highlight.Curvature) {{
                var crvShader = shader;
                gl.bindBuffer(gl.ARRAY_BUFFER, obj.curvatureBuffer);
                gl.vertexAttribPointer(crvShader.attrCurvature, 4, gl.FLOAT, false, 0, 0);
            }}
            else {{
                // ordinary and highlight shaders
                var s = shader;
                gl.bindBuffer(gl.ARRAY_BUFFER, obj.normalBuffer);
                gl.vertexAttribPointer(s.attrNormal, 3, gl.FLOAT, false, 0, 0);
            }}
            gl.bindBuffer(gl.ARRAY_BUFFER, obj.positionBuffer);
            gl.vertexAttribPointer(shader.attrPosition, 4, gl.FLOAT, false, 0, 0);
            gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, obj.indexBuffer);
            if (group.highlight === Highlight.Wireframe) {{
                // black wireframe
                gl.uniform4fv(shader.uniDiffuse, [0, 0, 0, 1]);
                gl.drawElements(gl.LINES, obj.indexBufferLength, gl.UNSIGNED_INT, 0);
            }}
            else {{
                gl.uniform4fv(shader.uniDiffuse, color);
                gl.drawElements(gl.TRIANGLES, obj.indexBufferLength, gl.UNSIGNED_INT, 0);
            }}
        }}
        
    }}
    if(group.showVisualNormals) {{
        var s = renderState.visualNormalShader;
        gl.useProgram(s.program);
        gl.uniformMatrix4fv(s.uniModelView, false, renderState.modelview.m);
        gl.uniformMatrix4fv(s.uniProjection, false, renderState.projection.m);
        gl.uniform1i(s.uniCrvMode, settings.curvatureType);
        gl.uniform1f(s.uniMaxCrv, settings.userMaxCrv);
        gl.uniform1f(s.uniMinCrv, settings.userMinCrv);
        gl.uniform1f(s.uniClipAmt, renderState.clipping);
        gl.uniform1i(s.uniShowCrv, group.highlight === Highlight.Curvature);
        gl.uniform1f(s.uniVizNormSize, group.visualNormalSize);
        gl.enableVertexAttribArray(s.attrVertexId);
        gl.enableVertexAttribArray(s.attrCurvature);
        for (var j = 0; j < group.objs.length; ++j) {{
            var obj = group.objs[j];
                gl.bindBuffer(gl.ARRAY_BUFFER, obj.duplacatedPointsBuffer);
                gl.vertexAttribPointer(s.attrPosition, 4, gl.FLOAT, false, 0, 0);
                gl.bindBuffer(gl.ARRAY_BUFFER, obj.duplicatedNormalsBuffer);
                gl.vertexAttribPointer(s.attrNormal, 3, gl.FLOAT, false, 0, 0);
                gl.bindBuffer(gl.ARRAY_BUFFER, obj.visualNormalVertexIdBuffer);
                gl.vertexAttribPointer(s.attrVertexId, 1, gl.FLOAT, false, 0, 0);
                gl.bindBuffer(gl.ARRAY_BUFFER, obj.duplicatedCurvatureBuffer);
                gl.vertexAttribPointer(s.attrCurvature, 4, gl.FLOAT, false, 0, 0);
                gl.drawArrays(gl.LINES, 0, obj.visualNormalBufferLength);

        }}
    }}
    
    if (group.highlight === Highlight.Curvature) {{
        var crvShader = shader;
        gl.disableVertexAttribArray(crvShader.attrCurvature);
    }}
    if (group.showControlMesh) {{
        gl.useProgram(renderState.shader.program);
        gl.disableVertexAttribArray(renderState.shader.attrNormal);
        // make the bounding box black
        gl.uniform4fv(renderState.shader.uniDiffuse, [0, 0, 0, 1]);
        gl.uniformMatrix4fv(renderState.shader.uniModelView, false, renderState.modelview.m);
        gl.uniformMatrix4fv(renderState.shader.uniProjection, false, renderState.projection.m);
        for (var j = 0; j < group.objs.length; ++j) {{
            var obj = group.objs[j];
            gl.bindBuffer(gl.ARRAY_BUFFER, obj.controlMesh.positionBuffer);
            gl.vertexAttribPointer(renderState.shader.attrPosition, 4, gl.FLOAT, false, 0, 0);
            gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, obj.controlMesh.indexBuffer);
            gl.drawElements(gl.LINES, obj.controlMesh.indexBufferLength, gl.UNSIGNED_INT, 0);
        }}
        gl.enableVertexAttribArray(renderState.shader.attrNormal);
    }}
}}
function setTessellationLevel(level) {{
    settings.tessellation = level;
    /*
    let menuitems = document.querySelectorAll('#patch-detail-menu a[data-value]');
    for(let i = 0; i < menuitems.length; i++) {{
        menuitems[i].className = menuitems[i].getAttribute('data-value') == String(level) ? 'checked' : '';
    }}
    */
    var menu = document.getElementById('select-patch-detail');
    menu.value = level.toString();
    for (var i = 0; i < renderState.groups.length; ++i) {{
        var group = renderState.groups[i];
        var objs = group.objs;
        for (var j = 0; j < objs.length; ++j) {{
            objs[j].evaluate(renderState.context, level);
        }}
        group.findMinMax();
    }}
    // update the global bounding box and curvature
    if (renderState.groups.length > 0) {{
        renderState.boundingBoxMin = renderState.groups[0].boundingBoxMin.dup();
        var boxMin = renderState.boundingBoxMin;
        renderState.boundingBoxMax = renderState.groups[0].boundingBoxMax.dup();
        var boxMax = renderState.boundingBoxMax;
        for (var k = 0; k < 4; ++k) {{
            renderState.globalGroup.minCrv[k] = renderState.groups[0].minCrv[k];
            renderState.globalGroup.maxCrv[k] = renderState.groups[0].maxCrv[k];
        }}
        for (var i = 1; i < renderState.groups.length; ++i) {{
            boxMin.x = Math.min(renderState.groups[i].boundingBoxMin.x, boxMin.x);
            boxMin.y = Math.min(renderState.groups[i].boundingBoxMin.y, boxMin.y);
            boxMin.z = Math.min(renderState.groups[i].boundingBoxMin.z, boxMin.z);
            boxMax.x = Math.max(renderState.groups[i].boundingBoxMax.x, boxMax.x);
            boxMax.y = Math.max(renderState.groups[i].boundingBoxMax.y, boxMax.y);
            boxMax.z = Math.max(renderState.groups[i].boundingBoxMax.z, boxMax.z);
            for (var k = 0; k < 4; ++k) {{
                renderState.globalGroup.minCrv[k] = Math.min(renderState.groups[i].minCrv[k], renderState.globalGroup.minCrv[k]);
                renderState.globalGroup.maxCrv[k] = Math.max(renderState.groups[i].maxCrv[k], renderState.globalGroup.maxCrv[k]);
            }}
        }}
    }}
    else {{
        renderState.boundingBoxMax.set(0.5, 0.5, 0.5);
        renderState.boundingBoxMin.set(-0.5, -0.5, -0.5);
        for (var k = 0; k < 4; ++k) {{
            renderState.globalGroup.minCrv[k] = 0;
            renderState.globalGroup.maxCrv[k] = 0;
        }}
    }}
    updateCurvatureClampIfDirty(renderState.globalGroup.minCrv[settings.curvatureType], renderState.globalGroup.maxCrv[settings.curvatureType]);
}}
function resetProjection() {{
    renderState.projection.setIdentity();
    renderState.modelview.setIdentity();
    renderState.aspectRatio = 1.0;
    renderState.translation = new Float32Array([0, 0, 0]);
    renderState.origin = new Float32Array([0, 0, 0]);
    renderState.rotation.set_axis_angle(3, 1, 1, 0.10).normalize4();
    renderState.scale = 1.0;
    renderState.zoom = 1.0;
    updateProjection();
    updateModelView();
}}
function freeGroups() {{
    for (var i = 0; i < renderState.groups.length; ++i) {{
        renderState.groups[i].free(renderState.context);
    }}
    renderState.groups = [];
}}
function selectGroup(index) {{
    if (index < 0 || index >= renderState.groups.length)
        index = -1;
    renderState.selectedGroupIndex = index;
    document.getElementById('select-group').value = index.toString();
    var nodes = document.getElementsByClassName('which-group-am-i-changing');
    for (var i = 0; i < nodes.length; ++i) {{
        while (nodes[i].firstChild) {{
            nodes[i].removeChild(nodes[i].firstChild);
        }}
        var s = (index == -1) ? 'Applying changes to all groups' : 'Applying changes to specific group: ' + renderState.groups[index].name;
        nodes[i].appendChild(document.createTextNode(s));
    }}
}}
// if the selected group was the global group then this
// changes the properties in all the other groups
function updateAllGroupsIfGlobal(propertyName) {{
    if (renderState.selectedGroupIndex != -1)
        return;
    var value = renderState.globalGroup[propertyName];
    for (var i = 0; i < renderState.groups.length; ++i) {{
        renderState.groups[i][propertyName] = value;
    }}
}}
function activeGroup() {{
    if (renderState.selectedGroupIndex >= 0 && renderState.selectedGroupIndex < renderState.groups.length)
        return renderState.groups[renderState.selectedGroupIndex];
    else
        return renderState.globalGroup;
}}
function updateGroups() {{
    var o = document.getElementById('select-group');
    while (o.firstChild) {{
        o.removeChild(o.firstChild);
    }}
    function addOption(index, group) {{
        var node = document.createElement('option');
        node.value = index.toString();
        node.appendChild(document.createTextNode(group.name));
        o.appendChild(node);
    }}
    addOption(-1, renderState.globalGroup);
    for (var i = 0; i < renderState.groups.length; ++i) {{
        addOption(i, renderState.groups[i]);
    }}
    if (renderState.selectedGroupIndex >= 0 && renderState.selectedGroupIndex < renderState.groups.length) {{
        o.value = renderState.selectedGroupIndex.toString();
    }}
    else {{
        o.value = '-1';
    }}
    var selectGroupColor = document.getElementById('select-group-color');
    selectGroupColor.value = activeGroup().color.toString();
}}
function loadBezierObject(text) {{
    freeGroups();
    renderState.groups = readBVFile(renderState.context, text);
    settingsRefreshFromGroup(renderState.globalGroup);
    setTessellationLevel(settings.tessellation);
    selectGroup(-1);
    updateGroups();
    resetProjection();
}}
function preload() {{
    var vssrc = `attribute vec4 inputPosition; 
				attribute vec3 inputNormal;

				uniform mat4 projection;
				uniform mat4 modelview;

				varying mediump vec4 position;
				varying mediump vec3 normal;

				void main() {{ 
					position = modelview * inputPosition;
					normal = normalize((modelview * vec4(inputNormal, 0.0)).xyz);
					gl_Position = projection * position;
				}}`;
    var totalCount = 8;
    var errorCount = 0;
    var fssrc = `#extension GL_OES_standard_derivatives : enable

				precision highp float;
				varying vec4 position;
				varying vec3 normal;

				uniform vec4 diffuse;
				uniform float clipAmt;
				uniform bool flatShading;
				uniform bool flipNormals;
				uniform vec3 lightsOn;

				const vec4 lightIntensity = vec4(1.0,1.0,1.0,1.0);
				const mat3 dirToLight = mat3(1,-1,1, -2.0,0,0, 0,1.5,0.1);
				const vec3 eye = vec3(0,0,1);

				void main() {{
					if (clipAmt != -55.0 && position.z < clipAmt) discard;
					vec3 n;
					if (flatShading) {{
						vec3 U = dFdx(position.xyz);
						vec3 V = dFdy(position.xyz);
						n = normalize(cross(U,V));
					}} else {{
						n = normalize(normal);
					}}
					
					if (flipNormals) {{
						n *= vec3(-1,-1,-1);
					}}
					float dI = 0.0;
					float sI = 0.0;
					for (int i = 0; i < 3; ++i) {{
						if (lightsOn[i] != 0.0) {{
							dI += clamp(dot( n, dirToLight[i]), 0.0, 1.0);
							sI += pow(clamp(dot( n, normalize((dirToLight[i] + eye) / 2.0)), 0.0, 1.0), 15.0);
						}}
					}}
					gl_FragColor = lightIntensity * diffuse * vec4(dI, dI, dI, 1.0) * 0.8
								+ lightIntensity * vec4(sI, sI, sI, 1.0) * diffuse * 0.5 + diffuse * 0.4;;

				}}


				`;
    var hlfssrc = `precision highp float;
					varying vec4 position;
					varying vec3 normal;

					uniform vec4 diffuse;
					uniform float clipAmt;
					uniform float highlightDensity;
					uniform float highlightResolution;
					uniform bool flipNormals;
					uniform vec3 lightsOn;

					const vec4 lightIntensity = vec4(1.0,1.0,1.0,1.0);
					const mat3 dirToLight = mat3(1,-1,1, -2.0,0,0, 0,1.5,0.1);
					const vec3 eye = vec3(0,0,1);
					const float ambient = 0.4;

					void main() {{
						if (clipAmt != -55.0 && position.z < clipAmt) discard;
						vec3 n = normalize(normal);
						if (flipNormals) {{
							n *= vec3(-1,-1,-1);
						}}
						float highlight = fract(dot( n, dirToLight[0]) * highlightResolution) > highlightDensity ? 0.5 : 1.0;
						float dI = 0.0;
						float sI = 0.0;
						for (int i = 0; i < 3; ++i) {{
							if (lightsOn[i] != 0.0) {{
								dI += clamp(dot( n, dirToLight[i]), 0.0, 1.0);
								sI += pow(clamp(dot( n, normalize((dirToLight[i] + eye) / 2.0)), 0.0, 1.0), 15.0);
							}}
						}}
						gl_FragColor =
							( (vec4(dI, dI, dI, 1.0) * 0.8 + vec4(sI, sI, sI, 1.0) * 0.5) * lightIntensity
							+ vec4(ambient,ambient,ambient,1.0)
							) * diffuse * highlight;
					}}
					`;
    var refl_fssrc = `precision highp float;
						varying vec4 position;
						varying vec3 normal;

						uniform vec4 diffuse;
						uniform bool flipNormals;
						uniform float clipAmt;
						uniform float highlightDensity;
						uniform float highlightResolution;
						uniform vec3 lightsOn;

						const vec4 lightIntensity = vec4(1.0,1.0,1.0,1.0);
						const mat3 dirToLight = mat3(1,-1,1, -2.0,0,0, 0,1.5,0.1);
						const vec3 eye = vec3(0,0,1);
						const float ambient = 0.4;

						void main() {{
							if (clipAmt != -55.0 && position.z < clipAmt) discard;
							vec3 n = normalize(normal);
							if (flipNormals) {{
								n *= vec3(-1,-1,-1);
							}}
							float highlight = fract(dot( n, eye) * highlightResolution) > highlightDensity ? 0.5 : 1.0;
							float dI = 0.0;
							float sI = 0.0;
							for (int i = 0; i < 3; ++i) {{
								if (lightsOn[i] != 0.0) {{
									dI += clamp(dot( n, dirToLight[i]), 0.0, 1.0);
									sI += pow(clamp(dot( n, normalize((dirToLight[i] + eye) / 2.0)), 0.0, 1.0), 15.0);
								}}
							}}
							gl_FragColor =
								( (vec4(dI, dI, dI, 1.0) * 0.8 + vec4(sI, sI, sI, 1.0) * 0.5) * lightIntensity
								+ vec4(ambient,ambient,ambient,1.0)
								) * diffuse * highlight;
						}}

						`;
    var curv_fssrc = `precision highp float;
					varying vec4 position;
					varying vec3 vColor;

					uniform vec4 diffuse;
					uniform float clipAmt;

					const vec4 lightIntensity = vec4(1.0,1.0,1.0,1.0);
					const vec3 dirToLight = vec3(1,-1,1);
					const vec3 eye = vec3(0,0,1);

					void main() {{
						if (clipAmt != -55.0 && position.z < clipAmt) discard;
						if (diffuse == vec4(0.0,0.0,0.0,1.0)) {{
							gl_FragColor = vec4(0.0,0.0,0.0,1.0);
						}} else {{
							gl_FragColor = vec4(vColor, 1.0);
						}}
					}}
					`;
    var curv_vssrc = `attribute vec4 inputPosition;
					attribute vec4 crv;

					uniform mat4 projection;
					uniform mat4 modelview;

					uniform int crvMode;
					uniform float maxCrv;
					uniform float minCrv;

					varying vec3 vColor;

					varying mediump vec4 position;

					vec3 crv2color(vec4 curvature) {{
						float c;
						vec3 colors[5];
						colors[0] = vec3(0.0, 0.0, 0.85);// blue
						colors[1] = vec3(0.0, 0.9, 0.9);// cyan
						colors[2] = vec3(0.0, 0.75, 0.0);// green
						colors[3] = vec3(0.9, 0.9, 0.0);// yellow
						colors[4] = vec3(0.85, 0.0, 0.0);// red
						vec3 max_out_color = vec3(0.9, 0.9, 0.9);
						vec3 min_out_color = vec3(0.1, 0.1, 0.1);
						if (crvMode == 0) {{
							c = curvature.x;
						}} else if (crvMode == 1) {{
							c = curvature.y;
						}} else if (crvMode == 2) {{
							c = curvature.z;
						}} else if (crvMode == 3) {{
							c = curvature.w;
						}}
						if (abs(maxCrv - minCrv) < 0.00001) {{
							c = 0.5;
						}} else if (c < minCrv - 0.00001) {{
							return min_out_color;
						}} else if (c > maxCrv + 0.00001) {{
							return max_out_color;
						}} else {{
							c = (c - minCrv) / (maxCrv - minCrv);
						}}
						if (c > 1.0)
							return max_out_color;
						else if (c < 0.0)
							return min_out_color;
						else if (c > 0.75)
							return (c - 0.75) / 0.25 * colors[4] + (1.0 - c) / 0.25 * colors[3];
						else if (c > 0.5)
							return (c - 0.5) / 0.25 * colors[3] + (0.75 - c) / 0.25 * colors[2];
						else if (c > 0.25)
							return (c - 0.25) / 0.25 * colors[2] + (0.5 - c) / 0.25 * colors[1];
						else if (c > 0.0)
							return (c) / 0.25 * colors[1] + (0.25 - c ) / 0.25 * colors[0];
						return colors[0];
					}}

					void main() {{
						position = modelview * inputPosition;
						vColor = crv2color(crv);
						gl_Position = projection * position;
					}}
					`;
    var normal_vssrc = `attribute vec4 inputPosition; 
					attribute vec3 inputNormal;
					attribute vec4 crv;
					attribute float vertexId;

					uniform mat4 projection;
					uniform mat4 modelview;
					uniform bool showCrv;
					uniform float minCrv;
					uniform float maxCrv;
					uniform int crvMode;
					uniform float vizNormSize;
					varying mediump vec4 position;

					varying mediump vec3 color;

					float crv2size(vec4 crv){{
						float c;
						if (crvMode == 0) {{
								c = crv.x;
							}} else if (crvMode == 1) {{
								c = crv.y;
							}} else if (crvMode == 2) {{
								c = crv.z;
							}} else if (crvMode == 3) {{
								c = crv.w;
							}}
							if (abs(maxCrv - minCrv) < 0.00001) {{
								c = 0.5;
							}} else if (c < minCrv - 0.00001) {{
								c=0.0;
							}} else if (c > maxCrv + 0.00001) {{
								c=1.0;
							}} else {{
								c = (c - minCrv) / (maxCrv - minCrv);
							}}
							return c;
					}}
					vec3 crv2color(vec4 curvature) {{
						float c;
						vec3 colors[5];
						colors[0] = vec3(0.0, 0.0, 0.85);// blue
						colors[1] = vec3(0.0, 0.9, 0.9);// cyan
						colors[2] = vec3(0.0, 0.75, 0.0);// green
						colors[3] = vec3(0.9, 0.9, 0.0);// yellow
						colors[4] = vec3(0.85, 0.0, 0.0);// red
						vec3 max_out_color = vec3(0.9, 0.9, 0.9);
						vec3 min_out_color = vec3(0.1, 0.1, 0.1);
						c = crv2size(curvature);
						if (c > 1.0)
							return max_out_color;
						else if (c < 0.0)
							return min_out_color;
						else if (c > 0.75)
							return (c - 0.75) / 0.25 * colors[4] + (1.0 - c) / 0.25 * colors[3];
						else if (c > 0.5)
							return (c - 0.5) / 0.25 * colors[3] + (0.75 - c) / 0.25 * colors[2];
						else if (c > 0.25)
							return (c - 0.25) / 0.25 * colors[2] + (0.5 - c) / 0.25 * colors[1];
						else if (c > 0.0)
							return (c) / 0.25 * colors[1] + (0.25 - c ) / 0.25 * colors[0];
						return colors[0];
					}}
					void main() {{ 
						vec4 p = crv;
						float c;
						if (!showCrv) {{
							c = 0.0;
						}} else{{
							c = crv2size(crv);
						}}
						if(vertexId == 0.0){{
							p = inputPosition;
						}}else{{
							p = vec4(vec3(inputPosition) - (inputNormal*(1.0 + c)*vizNormSize), 1.0);
						}}
						if (showCrv) {{
							color = crv2color(crv);
						}} else {{
							color = vec3(0);
						}}
						gl_Position = projection * modelview * p;
						position = modelview * inputPosition;
					}}`;
    var normal_fssrc = `precision highp float;
					varying vec4 position;
					varying mediump vec3 color;
					uniform float clipAmt;
					void main() {{
						if (clipAmt != -55.0 && position.z < clipAmt) discard;
						gl_FragColor = vec4(color, 1.0);
					}}`;
    setup(vssrc, fssrc, hlfssrc, refl_fssrc, curv_fssrc, curv_vssrc, normal_vssrc, normal_fssrc);
}}
function setup(vssrc, fssrc, hlfssrc, refl_fssrc, curv_fssrc, curv_vssrc, normal_vssrc, normal_fssrc) {{
    var canvas = document.getElementById('drawing');
    var gl = canvas.getContext('webgl');
    if (gl === null) {{
        window.alert('Your browser does not support WebGL');
        throw 'no webgl support';
    }}
    // extension needed for Uint32 index array
    var extA = gl.getExtension('OES_element_index_uint');
    // extension needed for flat shading
    var extB = gl.getExtension('OES_standard_derivatives');
    gl.enable(gl.DEPTH_TEST);
    gl.enable(gl.BLEND);
    gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
    gl.clearColor(0.0, 0.0, 0.0, 0.0);
    renderState.context = gl;
    var prog = makeProgram(gl, makeShader(gl, gl.VERTEX_SHADER, vssrc), makeShader(gl, gl.FRAGMENT_SHADER, fssrc));
    renderState.shader = {{
        program: prog,
        attrPosition: gl.getAttribLocation(prog, "inputPosition"),
        attrNormal: gl.getAttribLocation(prog, "inputNormal"),
        uniProjection: gl.getUniformLocation(prog, "projection"),
        uniClipAmt: gl.getUniformLocation(prog, "clipAmt"),
        uniModelView: gl.getUniformLocation(prog, "modelview"),
        uniDiffuse: gl.getUniformLocation(prog, "diffuse"),
        uniFlatShading: gl.getUniformLocation(prog, "flatShading"),
        uniFlipNormals: gl.getUniformLocation(prog, "flipNormals"),
        uniLightsOn: gl.getUniformLocation(prog, "lightsOn")
    }};
    prog = makeProgram(gl, makeShader(gl, gl.VERTEX_SHADER, vssrc), makeShader(gl, gl.FRAGMENT_SHADER, hlfssrc));
    renderState.highlightShader = {{
        program: prog,
        attrPosition: gl.getAttribLocation(prog, "inputPosition"),
        attrNormal: gl.getAttribLocation(prog, "inputNormal"),
        uniProjection: gl.getUniformLocation(prog, "projection"),
        uniClipAmt: gl.getUniformLocation(prog, "clipAmt"),
        uniModelView: gl.getUniformLocation(prog, "modelview"),
        uniDiffuse: gl.getUniformLocation(prog, "diffuse"),
        uniFlipNormals: gl.getUniformLocation(prog, "flipNormals"),
        uniLightsOn: gl.getUniformLocation(prog, "lightsOn"),
        uniHighLightDensity: gl.getUniformLocation(prog, "highlightDensity"),
        uniHighlightResolution: gl.getUniformLocation(prog, "highlightResolution")
    }};
    prog = makeProgram(gl, makeShader(gl, gl.VERTEX_SHADER, vssrc), makeShader(gl, gl.FRAGMENT_SHADER, refl_fssrc));
    renderState.reflectionShader = {{
        program: prog,
        attrPosition: gl.getAttribLocation(prog, "inputPosition"),
        attrNormal: gl.getAttribLocation(prog, "inputNormal"),
        uniProjection: gl.getUniformLocation(prog, "projection"),
        uniClipAmt: gl.getUniformLocation(prog, "clipAmt"),
        uniModelView: gl.getUniformLocation(prog, "modelview"),
        uniDiffuse: gl.getUniformLocation(prog, "diffuse"),
        uniFlipNormals: gl.getUniformLocation(prog, "flipNormals"),
        uniLightsOn: gl.getUniformLocation(prog, "lightsOn"),
        uniHighLightDensity: gl.getUniformLocation(prog, "highlightDensity"),
        uniHighlightResolution: gl.getUniformLocation(prog, "highlightResolution")
    }};
    prog = makeProgram(gl, makeShader(gl, gl.VERTEX_SHADER, curv_vssrc), makeShader(gl, gl.FRAGMENT_SHADER, curv_fssrc));
    renderState.curvatureShader = {{
        program: prog,
        attrCurvature: gl.getAttribLocation(prog, "crv"),
        attrPosition: gl.getAttribLocation(prog, "inputPosition"),
        uniProjection: gl.getUniformLocation(prog, "projection"),
        uniClipAmt: gl.getUniformLocation(prog, "clipAmt"),
        uniModelView: gl.getUniformLocation(prog, "modelview"),
        uniDiffuse: gl.getUniformLocation(prog, "diffuse"),
        uniCrvMode: gl.getUniformLocation(prog, "crvMode"),
        uniMaxCrv: gl.getUniformLocation(prog, "maxCrv"),
        uniMinCrv: gl.getUniformLocation(prog, "minCrv")
    }};
    prog = makeProgram(gl, makeShader(gl, gl.VERTEX_SHADER, normal_vssrc), makeShader(gl, gl.FRAGMENT_SHADER, normal_fssrc));
    renderState.visualNormalShader = {{
        program: prog,
        attrCurvature: gl.getAttribLocation(prog, "crv"),
        attrPosition: gl.getAttribLocation(prog, "inputPosition"),
        attrNormal: gl.getAttribLocation(prog, "inputNormal"),
        attrVertexId: gl.getAttribLocation(prog, "vertexId"),
        uniProjection: gl.getUniformLocation(prog, "projection"),
        uniClipAmt: gl.getUniformLocation(prog, "clipAmt"),
        uniModelView: gl.getUniformLocation(prog, "modelview"),
        uniCrvMode: gl.getUniformLocation(prog, "crvMode"),
        uniMaxCrv: gl.getUniformLocation(prog, "maxCrv"),
        uniMinCrv: gl.getUniformLocation(prog, "minCrv"),
        uniShowCrv: gl.getUniformLocation(prog, "showCrv"),
        uniVizNormSize: gl.getUniformLocation(prog, "vizNormSize")
    }};
    resizeCanvas(null);
    // these "wire cube" buffers are used for the bounding box
    wireCubeArrayBuffer = (function () {{
        var A = -0.5;
        var B = 0.5;
        var arr = new Float32Array([
            A, A, A, 1.0,
            A, A, B, 1.0,
            A, B, A, 1.0,
            A, B, B, 1.0,
            B, A, A, 1.0,
            B, A, B, 1.0,
            B, B, A, 1.0,
            B, B, B, 1.0,
        ]);
        var buffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ARRAY_BUFFER, arr, gl.STATIC_DRAW);
        return buffer;
    }})();
    wireCubeIndexBuffer = (function () {{
        var arr = new Uint32Array([
            0, 1, 1, 5, 5, 4, 4, 0,
            2, 3, 3, 7, 7, 6, 6, 2,
            2, 0, 3, 1, 7, 5, 6, 4
        ]);
        var buffer = gl.createBuffer();
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, arr, gl.STATIC_DRAW);
        return buffer;
    }})();
    InitColorDialogBox();
    selectGroup(-1);
    // default bezier object to appear
    loadBezierObject(`{bv_text}`);
    window.addEventListener('resize', resizeCanvas);
    window.requestAnimationFrame(draw);
    var mouseState = {{ x: 0, y: 0 }};
    // prevent context menu from appearing on right click
    canvas.addEventListener('contextmenu', function (e) {{
        e.preventDefault();
    }}, false);
    canvas.addEventListener('mousedown', function (e) {{
        if (e.button === 0 || e.button === 2)
            mouseState.x = e.clientX, mouseState.y = e.clientY;
    }});
    canvas.addEventListener('mousemove', function (e) {{
        if (e.buttons === 1) {{
            if (renderState.rotateMode) {{
                var x_angle = 0.01 * (e.clientY - mouseState.y) * Math.min(1.0, (1 / renderState.zoom));
                var x_rot = new Vec3();
                x_rot.set_axis_angle(1, 0, 0, -x_angle);
                var y_angle = 0.01 * (e.clientX - mouseState.x) * Math.min(1.0, (1 / renderState.zoom));
                var y_rot = new Vec3();
                y_rot.set_axis_angle(0, 1, 0, -y_angle);
                renderState.rotation.quaternion_mul(x_rot).quaternion_mul(y_rot);
                //renderState.rotation[1] -= 0.01 * (e.clientX - mouseState.x) * Math.min(1.0,(1/renderState.zoom));
                //renderState.rotation[0] -= 0.01 * (e.clientY - mouseState.y) * Math.min(1.0,(1/renderState.zoom));
                updateModelView();
            }}
            else {{
                renderState.clipping = (e.clientY / window.innerHeight) * 2.0 - 1.0;
            }}
            mouseState.x = e.clientX, mouseState.y = e.clientY;
        }}
        // panning when right clicking
        else if (e.buttons === 2) {{
            renderState.translation[1] -= (e.clientY - mouseState.y) / window.innerHeight * (1 / renderState.zoom);
            renderState.translation[0] += (e.clientX - mouseState.x) / window.innerWidth * (1 / renderState.zoom);
            updateModelView();
            mouseState.x = e.clientX, mouseState.y = e.clientY;
        }}
    }});
    var handleScroll = function (e) {{
		e.preventDefault();    // stop page scroll
  		e.stopPropagation();   // don't bubble outward
        function clamp(v) {{
            var amt = 0.25;
            if (v < -amt)
                return -amt;
            if (v > amt)
                return amt;
            return v;
        }}
        if (!e)
            e = event;
		const direction = e.deltaY < 0 ? 1 : -1;
        if (e.altKey) {{
            renderState.scale *= Math.pow(1.1, direction);
            updateModelView();
        }}
        else {{
            if (direction > 0) {{
                var dy = (e.clientY - canvas.height / 2) / window.innerHeight;
                var dx = (e.clientX - canvas.width / 2) / window.innerWidth;
                renderState.translation[1] += (clamp(dy) * (1 / renderState.zoom)) * 0.2;
                renderState.translation[0] -= (clamp(dx) * (1 / renderState.zoom)) * 0.2;
            }}
            renderState.zoom *= Math.pow(1.1, direction);
            updateProjection();
            updateModelView();
        }}
    }};
    canvas.addEventListener('wheel', handleScroll, {{ passive: false }});
    window.addEventListener('keydown', function (e) {{
        // angle = 10 degrees
        var angle = 0.174532925199430;
        switch (e.keyCode) {{
            case 81: {{
                // Q	
                var left = new Vec3();
                left.set_axis_angle(0, 0, 1, angle);
                renderState.rotation.quaternion_mul(left);
                updateModelView();
                break;
            }}
            case 69: {{
                // E
                var right = new Vec3();
                right.set_axis_angle(0, 0, 1, -angle);
                renderState.rotation.quaternion_mul(right);
                updateModelView();
                break;
            }}
            case 76: {{
                // L
                defaultSettings.showWatermark = !defaultSettings.showWatermark;
                if (defaultSettings.showWatermark) {{
                    canvas.style.backgroundColor = '';
                }}
                else {{
                    canvas.style.backgroundColor = 'rgb(255, 255, 255)';
                }}
                break;
            }}
            case 27:
                // ESC
                resetProjection();
                break;
        }}
    }});
    var menuitems = document.querySelectorAll('#patch-detail-menu a[data-value]');
    for (var i = 0; i < menuitems.length; i++) {{
        menuitems[i].addEventListener('click', function (e) {{
            var n = Number(e.target.getAttribute('data-value'));
            if (!isNaN(n))
                setTessellationLevel(n);
        }});
    }}
    setTessellationLevel(settings.tessellation);
    menuitems = document.querySelectorAll('#curv-detail-menu a[data-value]');
    for (var i = 0; i < menuitems.length; i++) {{
        menuitems[i].addEventListener('click', function (e) {{
            var type = Number(e.target.value);
            if (!isNaN(type))
                setCurvatureType(type);
        }});
    }}
    setCurvatureType(settings.curvatureType);
    document.getElementById('check-control-mesh').addEventListener('change', function (e) {{
        activeGroup().showControlMesh = e.target.checked;
        updateAllGroupsIfGlobal('showControlMesh');
    }});
    document.getElementById('check-flat-shading').addEventListener('change', function (e) {{
        activeGroup().flatShading = e.target.checked;
        updateAllGroupsIfGlobal('flatShading');
    }});
    document.getElementById('check-flip-normals').addEventListener('change', function (e) {{
        activeGroup().flipNormals = e.target.checked;
        updateAllGroupsIfGlobal('flipNormals');
    }});
    document.getElementById('check-light-1').addEventListener('change', function (e) {{
        settings.lightsOn[0] = e.target.checked ? 1.0 : 0.0;
    }});
    document.getElementById('check-light-2').addEventListener('change', function (e) {{
        settings.lightsOn[1] = e.target.checked ? 1.0 : 0.0;
    }});
    document.getElementById('check-light-3').addEventListener('change', function (e) {{
        settings.lightsOn[2] = e.target.checked ? 1.0 : 0.0;
    }});
    var checkHighlightBox = document.getElementById('check-highlight');
    var checkReflectionBox = document.getElementById('check-reflection');
    var checkCurvatureBox = document.getElementById('check-curvature');
    var checkWireframeBox = document.getElementById('check-wireframe');
    var checkVisualNormalsBox = document.getElementById('check-visualize_normals');
    var updateHighlightMode = function (e) {{
        var lines = checkHighlightBox.checked;
        var refl = checkReflectionBox.checked;
        var curv = checkCurvatureBox.checked;
        var wire = checkWireframeBox.checked;
        // count of number of boxes checked
        var count = (lines ? 1 : 0) + (refl ? 1 : 0) + (curv ? 1 : 0) + (wire ? 1 : 0);
        // if more than one box checked, disable all but the most recent
        if (count > 0) {{
            checkHighlightBox.checked = false;
            checkReflectionBox.checked = false;
            checkCurvatureBox.checked = false;
            checkWireframeBox.checked = false;
            e.target.checked = true;
            lines = checkHighlightBox.checked;
            refl = checkReflectionBox.checked;
            curv = checkCurvatureBox.checked;
            wire = checkWireframeBox.checked;
        }}
        if (lines) {{
            activeGroup().highlight = Highlight.Line;
        }}
        else if (refl) {{
            activeGroup().highlight = Highlight.Refelection;
        }}
        else if (curv) {{
            activeGroup().highlight = Highlight.Curvature;
        }}
        else if (wire) {{
            activeGroup().highlight = Highlight.Wireframe;
        }}
        else {{
            activeGroup().highlight = Highlight.Normal;
        }}
        updateAllGroupsIfGlobal('highlight');
    }};
    document.getElementById('check-bounding-box').addEventListener('change', function (e) {{
        settings.showBoundingBox = e.target.checked;
    }});
    document.getElementById('check-patches').addEventListener('change', function (e) {{
        activeGroup().showPatches = e.target.checked;
        updateAllGroupsIfGlobal('showPatches');
    }});
    checkHighlightBox.addEventListener('change', updateHighlightMode);
    checkReflectionBox.addEventListener('change', updateHighlightMode);
    checkCurvatureBox.addEventListener('change', updateHighlightMode);
    checkWireframeBox.addEventListener('change', updateHighlightMode);
    checkVisualNormalsBox.addEventListener('change', function (e) {{
        activeGroup().showVisualNormals = e.target.checked;
        updateAllGroupsIfGlobal('showVisualNormals');
    }});
    document.getElementById('rotateModeTrue').addEventListener('change', function (e) {{
        renderState.rotateMode = e.target.checked;
    }});
    document.getElementById('rotateModeFalse').addEventListener('change', function (e) {{
        renderState.rotateMode = !e.target.checked;
    }});
    document.getElementById('select-curv-type').addEventListener('change', function (e) {{
        var n = Number(e.target.value);
        if (!isNaN(n))
            setCurvatureType(n);
    }});
    document.getElementById('select-patch-detail').addEventListener('change', function (e) {{
        var n = Number(e.target.value);
        if (!isNaN(n))
            setTessellationLevel(n);
    }});
    document.getElementById('select-group').addEventListener('change', function (e) {{
        selectGroup(Number(e.target.value));
        var selectGroupColor = document.getElementById('select-group-color');
        if (renderState.selectedGroupIndex >= 0 && renderState.selectedGroupIndex < renderState.groups.length) {{
            var group = renderState.groups[renderState.selectedGroupIndex];
            selectGroupColor.value = group.color.toString();
        }}
        else {{
            selectGroupColor.value = '0';
        }}
        settingsRefreshFromGroup(activeGroup());
    }});
    document.getElementById('select-group-color').addEventListener('change', function (e) {{
        activeGroup().color = Number(e.target.value);
        updateAllGroupsIfGlobal('color');
    }});
    document.getElementById('range-highlight-density').addEventListener('input', function (e) {{
        activeGroup().highlightDensity = Number(e.target.value);
        document.getElementById('range-highlight-density-value').textContent = e.target.value;
        updateAllGroupsIfGlobal('highlightDensity');
    }});
    document.getElementById('range-visual-normal-size').addEventListener('input', function (e) {{
        activeGroup().visualNormalSize = Number(e.target.value);
        document.getElementById('range-visual-normal-size-value').textContent = e.target.value;
        updateAllGroupsIfGlobal('visualNormalSize');
    }});
    document.getElementById('range-highlight-resolution').addEventListener('input', function (e) {{
        activeGroup().highlightResolution = Number(e.target.value);
        document.getElementById('range-highlight-resolution-value').textContent = e.target.value;
        updateAllGroupsIfGlobal('highlightResolution');
    }});
    document.getElementById('delete-group').addEventListener('click', function (e) {{
        if (renderState.selectedGroupIndex < 0 || renderState.selectedGroupIndex >= renderState.groups.length)
            return;
        activeGroup().free(renderState.context);
        renderState.groups.splice(renderState.selectedGroupIndex, 1);
        selectGroup(renderState.selectedGroupIndex - 1);
        updateGroups();
    }});
    // curvature clamping
    (function () {{
        var a = document.getElementById('min-crv-in');
        var b = document.getElementById('max-crv-in');
        var restoreBtn = document.getElementById('restore-crv-in');
        a.addEventListener('change', function (e) {{
            var val = Number(a.value);
            if (isNaN(val)) {{
                a.value = renderState.globalGroup.minCrv[settings.curvatureType].toString();
                return;
            }}
            if (val > Number(b.value)) {{
                b.value = val.toString();
            }}
            restoreBtn.disabled = false;
            settings.userMinCrv = val;
        }});
        b.addEventListener('change', function (e) {{
            var val = Number(b.value);
            if (isNaN(val)) {{
                b.value = renderState.globalGroup.maxCrv[settings.curvatureType].toString();
                return;
            }}
            if (val < Number(a.value)) {{
                a.value = val.toString();
            }}
            restoreBtn.disabled = false;
            settings.userMaxCrv = val;
        }});
        restoreBtn.addEventListener('click', function () {{
            settings.userMinCrv = renderState.globalGroup.minCrv[settings.curvatureType];
            settings.userMaxCrv = renderState.globalGroup.maxCrv[settings.curvatureType];
            a.value = settings.userMinCrv.toString();
            b.value = settings.userMaxCrv.toString();
            restoreBtn.disabled = true;
        }});
    }})();
}}
function InitColorDialogBox() {{
    var tmp = document.getElementById('select-group-color');
    for (var i = 0; i < GroupColors.length; ++i) {{
        var el = document.createElement('option');
        el.textContent = GroupColors[i].name;
        el.value = i.toString();
        tmp.appendChild(el);
    }}
}}
function resizeCanvas(e) {{
    var canvas = renderState.context.canvas;
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    updateProjection();
}}
// curvature clamping
function updateCurvatureClampIfDirty(low, high) {{
    var a = document.getElementById('min-crv-in');
    var b = document.getElementById('max-crv-in');
    var restoreBtn = document.getElementById('restore-crv-in');
    if (restoreBtn.disabled) {{
        a.value = low.toString();
        b.value = high.toString();
        settings.userMinCrv = low;
        settings.userMaxCrv = high;
    }}
    function set_to(id, val) {{
        var obj = document.getElementById(id);
        while (obj.firstChild) {{
            obj.removeChild(obj.firstChild);
        }}
        obj.appendChild(document.createTextNode(val.toString()));
    }}
    set_to('min-crv-actual', low);
    set_to('max-crv-actual', high);
}}
function setCurvatureType(type) {{
    var menuitems = document.querySelectorAll('#curv-detail-menu a[data-value]');
    for (var i = 0; i < menuitems.length; i++) {{
        menuitems[i].className = menuitems[i].getAttribute('data-value') == String(type) ? 'checked' : '';
    }}
    settings.curvatureType = type;
    updateCurvatureClampIfDirty(renderState.globalGroup.minCrv[settings.curvatureType], renderState.globalGroup.maxCrv[settings.curvatureType]);
}}
window.addEventListener('load', preload);

	</script>
    <script>
		function savedPositionsRefresh(after) {{
    var o = document.getElementById('select-load-position');
    while (o.hasChildNodes()) {{
        o.removeChild(o.lastChild);
    }}
    for (var i = 0; i < savedPositions.length; ++i) {{
        var option = document.createElement('option');
        option.value = i.toString();
        option.appendChild(document.createTextNode('Position ' + savedPositions[i].id));
        o.appendChild(option);
    }}
    o.value = after.toString();
}}
function settingsRefreshFromGroup(group) {{
    var hlLine = false;
    var hlRefl = false;
    var hlCurv = false;
    var hlWire = false;
    switch (group.highlight) {{
        case Highlight.Normal:
            break;
        case Highlight.Line:
            hlLine = true;
            break;
        case Highlight.Refelection:
            hlRefl = true;
            break;
        case Highlight.Curvature:
            hlCurv = true;
            break;
        case Highlight.Wireframe:
            hlWire = true;
            break;
    }}
    document.getElementById('check-highlight').checked = hlLine;
    document.getElementById('check-reflection').checked = hlRefl;
    document.getElementById('check-curvature').checked = hlCurv;
    document.getElementById('check-wireframe').checked = hlWire;
    document.getElementById('check-visualize_normals').checked = group.showVisualNormals;
    document.getElementById('check-patches').checked = group.showPatches;
    document.getElementById('range-highlight-density').value = group.highlightDensity.toString();
    document.getElementById('range-highlight-resolution').value = group.highlightResolution.toString();
    document.getElementById('range-visual-normal-size').value = group.visualNormalSize.toString();
    document.getElementById('check-flat-shading').checked = group.flatShading;
    document.getElementById('check-flip-normals').checked = group.flipNormals;
    document.getElementById('check-control-mesh').checked = group.showControlMesh;
}}
function settingsUIRefresh() {{
    document.getElementById('check-light-1').checked = settings.lightsOn[0] != 0.0;
    document.getElementById('check-light-2').checked = settings.lightsOn[1] != 0.0;
    document.getElementById('check-light-3').checked = settings.lightsOn[2] != 0.0;
    document.getElementById('check-bounding-box').checked = settings.showBoundingBox;
}}
function addMyEventListeners() {{
    document.getElementById('btn-reset').addEventListener('click', function (e) {{
        resetProjection();
    }});
    document.getElementById('remove-position').addEventListener('click', function (e) {{
        var index = Number(document.getElementById('select-load-position').value);
        if (index >= 0) {{
            savedPositions.splice(index, 1);
            savedPositionsRefresh(index - 1);
        }}
    }});
    // TODO also save curvature type
    var savedPositionsCount = 0;
    var parse_f32_arr = function (obj) {{
        var arr = [0, 1, 2];
        arr[0] = Number(obj[0]);
        arr[1] = Number(obj[1]);
        arr[2] = Number(obj[2]);
        if(3 in obj) {{
            arr[3] = Number(obj[3]);
        }}
        return new Float32Array(arr);
    }};
    var parse_mat4 = function (obj) {{
        var ret = new Mat4();
        obj = obj.m;
        for (var i in obj) {{
            ret.m[i] = Number(obj[i]);
        }}
        return ret;
    }};
    document.getElementById('save-position').addEventListener('click', function (e) {{
        ++savedPositionsCount;
        savedPositions.push({{
            id: savedPositionsCount,
            translation: new Float32Array(renderState.translation),
            rotation: new Float32Array([renderState.rotation.x, renderState.rotation.y, renderState.rotation.z, renderState.rotation.d]),
            zoom: renderState.zoom,
            scale: renderState.scale,
            projection: (new Mat4()).copy(renderState.projection),
            modelview: (new Mat4()).copy(renderState.modelview),
            setting_flatShading: renderState.globalGroup.flatShading,
            setting_flipNormals: renderState.globalGroup.flipNormals,
            setting_showControlMesh: renderState.globalGroup.showControlMesh,
            setting_showPatches: renderState.globalGroup.showPatches,
            setting_highlight: renderState.globalGroup.highlight,
            setting_showBoundingBox: settings.showBoundingBox,
            settings_showVisualNormals: renderState.globalGroup.showVisualNormals,
            setting_highlightDensity: renderState.globalGroup.highlightDensity,
            setting_highlightResolution: renderState.globalGroup.highlightResolution,
            setting_visualNormalSize: renderState.globalGroup.visualNormalSize,
            setting_lightsOn0: settings.lightsOn[0],
            setting_lightsOn1: settings.lightsOn[1],
            setting_lightsOn2: settings.lightsOn[2]
        }});
        savedPositionsRefresh(savedPositions.length - 1);
    }});
    var lastSavedPosition = 0;
    var loadSavedPosition = function (index) {{
        if (index < 0 || index >= savedPositions.length)
            return;
        lastSavedPosition = index;
        var s = savedPositions[index];
        renderState.rotation.x = s.rotation[0];
        renderState.rotation.y = s.rotation[1];
        renderState.rotation.z = s.rotation[2];
        renderState.rotation.d = s.rotation[3];
        renderState.translation = new Float32Array(s.translation);
        renderState.projection = Mat4.makeCopy(s.projection);
        renderState.modelview = Mat4.makeCopy(s.modelview);
        renderState.zoom = s.zoom;
        renderState.scale = s.scale;
        renderState.globalGroup.flatShading = s.setting_flatShading;
        renderState.globalGroup.flipNormals = s.setting_flipNormals;
        renderState.globalGroup.showControlMesh = s.setting_showControlMesh;
        renderState.globalGroup.showPatches = s.setting_showPatches;
        renderState.globalGroup.highlight = s.setting_highlight;
        renderState.globalGroup.showVisualNormals = s.settings_showVisualNormals;
        settings.showBoundingBox = s.setting_showBoundingBox;
        renderState.globalGroup.highlightDensity = s.setting_highlightDensity;
        renderState.globalGroup.highlightResolution = s.setting_highlightResolution;
        renderState.globalGroup.visualNormalSize = s.setting_visualNormalSize;
        settings.lightsOn[0] = s.setting_lightsOn0;
        settings.lightsOn[1] = s.setting_lightsOn1;
        settings.lightsOn[2] = s.setting_lightsOn2;
        selectGroup(-1);
        for (var i = 0; i < renderState.groups.length; ++i) {{
            renderState.groups[i].flatShading = s.setting_flatShading;
            renderState.groups[i].flipNormals = s.setting_flipNormals;
            renderState.groups[i].showControlMesh = s.setting_showControlMesh;
            renderState.groups[i].showPatches = s.setting_showPatches;
            renderState.groups[i].highlight = s.setting_highlight;
            renderState.groups[i].showVisualNormals = s.settings_showVisualNormals;
            renderState.groups[i].highlightDensity = s.setting_highlightDensity;
            renderState.groups[i].highlightResolution = s.setting_highlightResolution;
            renderState.groups[i].visualNormalSize = s.setting_visualNormalSize;
        }}
        settingsUIRefresh();
        settingsRefreshFromGroup(renderState.globalGroup);
        updateProjection();
        updateModelView();
    }};
    document.getElementById('select-load-position').addEventListener('change', function (e) {{
        var index = Number(e.srcElement.value);
        // this check is to prevent NaN
        if (index >= 0) {{
            loadSavedPosition(index);
        }}
    }});
    document.getElementById('select-load-position').addEventListener('click', function (e) {{
        if (e.srcElement.length == 1) {{
            loadSavedPosition(0);
        }}
    }});
    document.getElementById('restore-load-position').addEventListener('click', function (e) {{
        loadSavedPosition(lastSavedPosition);
    }});
    function loadSettings() {{
        var stored = false;
        if (stored) {{
            // parse stored settings
            var obj = JSON.parse(stored);
            for (var i = 0; i < obj.length; ++i) {{
                obj[i].translation = parse_f32_arr(obj[i].translation);
                obj[i].rotation = parse_f32_arr(obj[i].rotation);
                obj[i].projection = parse_mat4(obj[i].projection);
                obj[i].modelview = parse_mat4(obj[i].modelview);
            }}
            savedPositions = obj;
            savedPositionsCount = obj.length;
        }}
        settings = defaultSettings;
        savedPositionsRefresh(0);
        settingsUIRefresh();
    }}
    window.addEventListener('load', loadSettings);
}}
addMyEventListeners();
    // setup hover menu
    var currently_displayed_menu = null;
    function close_menu() {{
        if (currently_displayed_menu) {{
            currently_displayed_menu.style.display = 'none';
        }}
        currently_displayed_menu = null;
    }}
    function show_obj(obj) {{
        close_menu();
        obj.style.display = 'block';
        currently_displayed_menu = obj;
    }}
    function link_objects(obj_a, obj_b) {{
        obj_a.addEventListener('mouseover', function () {{
            show_obj(obj_b);
        }});
    }}
    var menuIDs = [
        'shader-settings', 'curvature', 'display', 'groups', 'other', 'help'
    ];
    for (var i = 0; i < menuIDs.length; ++i) {{
        var obj_a = document.getElementById('top-level-' + menuIDs[i]);
        var obj_b = document.getElementById('bottom-level-' + menuIDs[i]);
        link_objects(obj_a, obj_b);
    }}
    var all_canvas = document.getElementsByTagName('canvas');
    for (var i = 0; i < all_canvas.length; ++i) {{
        // click and mousedown seem like they would be the same but they are not
        all_canvas[i].addEventListener('click', close_menu);
        all_canvas[i].addEventListener('mousedown', close_menu);
    }}

	</script>
  </body>
</html>

    """
    p = Path("bv_tmp.html")
    p.write_text(html_code, encoding="utf-8")
    frame = IFrame("bv_tmp.html", width=width, height=height)
    return frame



def display_bv_file(filename, width=800, height=400):
    """
    Display a bv file.
    Args:
        filename (str): The path to the bv file.
        width (int): The width of the display frame.
        height (int): The height of the display frame.
    """
    bv_text = Path(filename).read_text(encoding="utf-8")
    return display_bv_string(bv_text, width, height)

