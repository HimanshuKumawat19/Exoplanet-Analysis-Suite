# Project Guardian: Dataset Guide

This document provides the steps to download the asteroid data and a detailed description of each attribute in the dataset.

## How to Download Your Mission Data

Follow these steps to generate and download the specific CSV file needed for this project from the official NASA/JPL source.

1. **Go to the JPL Database:** Open the [JPL Small-Body Database Search Engine](https://ssd.jpl.nasa.gov/tools/sbdb_query.html "null").
    
2. **Clear Existing Fields:** If the "Output Fields" box on the right is not empty, click **"deselect all"** and then **"remove"** to clear it.
    
3. **Add Data Presets:**
    
    - From the "Output Field Preset Selector" dropdown, choose **"physical parameters for asteroids"** and click **"apply"**.
        
    - Open the dropdown again, choose **"osculating orbital elements (asteroid-style)"** and click **"apply"**.
        
4. **Select Final Fields:** Review the "Output Fields" box. Make sure only the 15 attributes listed in the guide below are checked. Deselect any others.
    
5. **Generate and Download:**
    
    - Scroll to the bottom of the page.
        
    - Under "Output Format," ensure **"CSV (comma-separated values)"** is selected.
        
    - Click the green **"Get Results"** button (or "Generate Table").
        
    - Rename the downloaded file to `project_guardian_data.csv`.
        

## Dataset Attributes (The "What's What" Guide)

This dataset is a census of known asteroids, containing their physical, orbital, and observational characteristics. Here's a breakdown of each attribute you've selected.

|   |   |   |
|---|---|---|
|**Attribute Name**|**What It Means**|**Why It's Important for Our Mission**|
|**Identification Fields**|||
|`object fullname`|The unique name or designation of the asteroid.|To identify and label each object in our analysis.|
|`PHA`|**P**otentially **H**azardous **A**steroid flag (Y/N).|**This is our main target variable for predicting threats.**|
|**Physical Fields**|||
|`H`|Absolute Magnitude (a measure of brightness).|A key predictor for estimating an asteroid's size.|
|`diameter`|The estimated diameter in kilometers (km).|A perfect **target** for our regression model to predict size.|
|`albedo`|The fraction of light the surface reflects.|Helps our models guess the asteroid's composition (e.g., dark and rocky vs. bright and icy).|
|`rot_per`|Rotation Period (how fast it spins in hours).|An interesting feature that might help classify different types of asteroids.|
|`spec_T`|Spectral Type (Tholen classification).|A label describing the asteroid's composition. A great **target** for a classification model.|
|**Orbital Fields**|||
|`e`|Eccentricity (the shape of the orbit).|A critical predictor. Orbits with high eccentricity are more likely to cross paths with planets.|
|`a`|Semi-Major Axis (the size of the orbit).|Defines how large the asteroid's path around the sun is.|
|`i`|Inclination (the tilt of the orbit).|High inclination orbits are less likely to intersect with Earth's orbital plane.|
|`Earth MOID (au)`|**M**inimum **O**rbit **I**ntersection **D**istance.|The closest the asteroid's orbit ever gets to Earth's orbit. **Vital for threat assessment.**|
|`orbit_class`|The family or group the asteroid belongs to.|A very useful categorical feature that helps our models understand the object's neighborhood.|
|**Observational Fields**|||
|`condition_code`|A score (0-9) for the orbit's quality/uncertainty.|A great **target** for predicting how reliable an asteroid's calculated path is.|
|`data-arc span`|The number of days the asteroid has been observed.|A key predictor for the `condition_code`. Longer observation arcs mean more reliable orbits.|
|`# obs. used (total)`|The total number of observations of the asteroid.|Another key predictor for orbit reliability. More observations lead to better orbit calculations.|