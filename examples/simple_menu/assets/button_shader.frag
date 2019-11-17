uniform vec4 rect;
uniform float hover_progress;
uniform vec4 hover_color;
uniform float click_progress;
uniform vec4 click_color;
uniform vec2 click_pos;

varying vec4 main_color;
varying vec2 position;


void main() {
    vec2 uv = (gl_FragCoord.xy - rect.xy) / rect.zw;
    uv.x - (hover_progress-2.0)*.5;
    vec4 col = mix(hover_color, main_color, sign(uv.x - hover_progress));
    col = mix(click_color, col, smoothstep(0.05, 0.9, distance(gl_FragCoord.xy, click_pos)-click_progress*rect.z));

    gl_FragColor = col;
}