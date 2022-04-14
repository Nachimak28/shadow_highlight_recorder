# A Shadow & Highlight image modifier and recorder for image enhancement analysis

## Preprocessing
Change csv path in config.py

Make the CSV file in the following format with some default value initialization:

| image_paths | status | shadow_amount_percent | shadow_tone_percent | shadow_radius | highlight_amount_percent | highlight_tone_percent | highlight_radius | color_percent |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| full/path/to/a.png | pending | 0.0 | 0.0 | 100 | 0.0 | 0.0 | 100 | 1 |
| full/path/to/b.png | pending | 0.0 | 0.0 | 100 | 0.0 | 0.0 | 100 | 1 |
| full/path/to/c.png | pending | 0.0 | 0.0 | 100 | 0.0 | 0.0 | 100 | 1 |
| full/path/to/d.png | pending | 0.0 | 0.0 | 100 | 0.0 | 0.0 | 100 | 1 |
| full/path/to/e.png | pending | 0.0 | 0.0 | 100 | 0.0 | 0.0 | 100 | 1 |


## Running the code
Clone this repo

```
cd shadow_highlight_recorder

cd src

streamlit run app.py
```

**Features:**
* Resumability from where we left last time if done in multiple sessions
* Histograms of updated image
* Pending and Completed Count
* Modular enough to easily modify and reuse
* Save intermediate data to satisfy the OCD of developers to constantly save work


![Demo](assets/app_demo.gif)