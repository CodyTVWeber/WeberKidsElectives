% Twinkle Twinkle Little Star - Simple melody in C major
\version "2.24.0"
\header {
  title = "Twinkle Twinkle Little Star"
  subtitle = "Simple Melody (C Major)"
  composer = "Traditional"
}

melody = \relative c' {
  \key c \major
  \time 4/4
  c4 c g' g a a g2 |
  f4 f e e d d c2 |
  g'4 g f f e e d2 |
  g4 g f f e e d2 |
  c4 c g' g a a g2 |
  f4 f e e d d c2 \bar "|." |
}

\score {
  \new Staff { \clef treble \melody }
  \layout { }
  \midi { }
}

