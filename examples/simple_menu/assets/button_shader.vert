varying vec4 main_color;
varying vec2 position;

void main() {
    main_color = gl_Color;
    vec4 pos = gl_ProjectionMatrix * gl_ModelViewMatrix * gl_Vertex;
    position = pos.xy;
    gl_Position = pos;
}