# Personal Data Retriever

A minimalist Python implementation for structured data access.

## 📁 Source Architecture
This project utilizes a procedural programming approach to handle user input and data retrieval. It is designed for simplicity and efficiency in querying specific biographical attributes.

### Data Mapping
The application routes user input through a series of conditional gates:
- **Identifier:** `name`, `age`
- **Contextual:** `job`, `city`
- **Preference:** `hobby`
- **Aggregate:** `father + tell` (Profile summary function)

## ⚙️ Logic Flow
```text
[Input] -> [Normalization] -> [Heuristic Matching] -> [Output]
                                      |
                           [Invalid Input Fallback]
