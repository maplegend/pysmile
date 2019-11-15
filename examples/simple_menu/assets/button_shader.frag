uniform float x_coord;
uniform vec4 color;
uniform vec4 rect;
varying vec4 main_color;
varying vec2 position;


void main() {
    vec2 uv = (gl_FragCoord.xy - rect.xy) / rect.zw;///size;
    vec4 col = mix(main_color, color, uv.x - x_coord);

    gl_FragColor = col;
}