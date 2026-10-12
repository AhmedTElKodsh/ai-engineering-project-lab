# Support intake development fixtures

Seven scenario patterns and eight deliberately bad output payloads. These are visible teaching/development cases, not hidden assessments or measured model results. The learner implements the parser, chosen strict schema, source checks and review behavior; no extractor is supplied here.

Start with absence, negation and a bad span; add uncertainty, chronology and instruction-like input before J1 completion. The English/Arabic pair has matching expected fields, but one pair cannot establish broad bilingual quality. Use unfamiliar cases separately for ownership assessment.

Coordinates are start-inclusive/end-exclusive code-point indices into the original unnormalized Python str. Read UTF-8 and preserve LF. Bytes and grapheme positions are different. The Arabic quote includes a combining mark; stripping it breaks the original coordinate contract. A matching quote proves position, not support for the associated value.

The payload matrix separates malformed JSON, wrong types, missing fields, extra fields, unsupported values with real evidence, wrong positions, empty output omitting stated facts, and schema-valid obedience to injected source text. A strict schema cannot detect every semantic error. The instruction-like case is untrusted source content and must never become approval.

`python tools/test_supportops.py` validates fixture integrity only. It does not call a model, implement application rules, execute the tutor, or demonstrate learner mastery.
