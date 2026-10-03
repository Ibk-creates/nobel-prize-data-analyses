[README.md](https://github.com/user-attachments/files/33012485/README.md)
# Nobel Prize Analysis

A DataCamp project that analyzes Nobel Prize winner data with Python and pandas to uncover patterns in who wins, where they are from, and when.

## Questions Answered

1. **What is the most commonly awarded gender and birth country?**
   Stored as the strings `top_gender` and `top_country`.

2. **Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?**
   Stored as the integer `max_decade_usa`.

3. **Which decade and Nobel Prize category combination had the highest proportion of female laureates?**
   Stored as the dictionary `max_female_dict`, with the decade as the key and the category as the value (a single key:value pair).

4. **Who was the first woman to receive a Nobel Prize, and in what category?**
   Stored as the strings `first_woman_name` and `first_woman_category`.

5. **Which individuals or organizations have won more than one Nobel Prize throughout the years?**
   Stored as the list `repeat_list` (full names).

## Tech Stack

- Python 3
- pandas

## Getting Started

### Prerequisites

```bash
pip install pandas
```

### Installation

```bash
git clone https://github.com/ibk-creates/nobel-prize-data-analyses.git
cd nobel-prize-data-analyses
```

### Run

```bash
python "nobel prize.py"
```

## Dataset

The project uses a Nobel Prize laureates dataset provided by DataCamp (`nobel.csv`). Key columns used include `year`, `category`, `sex`, `birth_country`, `full_name`, and `female_laureates`.

## Results

| Variable | Description |
|---|---|
| `top_gender` | Most commonly awarded gender |
| `top_country` | Most common birth country |
| `max_decade_usa` | Decade with the highest share of US-born winners |
| `max_female_dict` | Decade and category with the highest proportion of female laureates |
| `first_woman_name` | First woman to win a Nobel Prize |
| `first_woman_category` | Category of that first prize |
| `repeat_list` | Individuals or organizations with more than one Nobel Prize |

## Author

**Ibukun**
GitHub: [@ibk-creates](https://github.com/ibk-creates)
