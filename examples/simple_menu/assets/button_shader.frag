uniform vec4 rect;
uniform float hover_progress;
uniform vec4 hover_color;
uniform float click_progress;
uniform vec4 click_color;
uniform vec2 click_pos;

varying vec4 main_color;
varying vec2 position;


void main() {
    vec2 uv = (gl_FragCoord.xy - rect.xy ) / rect.zw;
    vec2 pos = (click_pos - rect.xy) / rect.zw;
    vec4 col = mix(hover_color, main_color, uv.x - (hover_progress-1.0));
    col = mix(click_color, col, step(0.1, distance(pos, uv)-click_progress));

    gl_FragColor = col;
}