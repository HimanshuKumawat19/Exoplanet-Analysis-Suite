# Exoplanet Data Dictionary (Project Cheat Sheet)

This is a guide to the most important columns in the `PSCompPars` dataset for our project: **Predicting the `discoverymethod`**.

### Category 1: Identifiers (The "Names")

- **Project Use:** For labeling, debugging, and merging data.
    
- **Model Use:** **DO NOT** use these as features to train your model.
    

|   |   |   |
|---|---|---|
|**Column Name**|**Datatype (in Pandas)**|**Easy Explanation**|
|`pl_name`|`object` (text)|The planet's unique name (e.g., "Kepler-186 f").|
|`hostname`|`object` (text)|The name of the host star the planet orbits (e.g., "Kepler-186").|
|`pl_letter`|`object` (text)|The letter ('b', 'c', 'd'...) that identifies the planet in its system.|
|`rowid`|`int64` (integer)|A unique number for each row in the table.|

### Category 2: The Target (Y)

- **Project Use:** This is the "answer" our model is trying to learn.
    
- **Model Use:** This is the **Target variable (Y)**.
    

|   |   |   |
|---|---|---|
|**Column Name**|**Datatype (in Pandas)**|**Easy Explanation**|
|`discoverymethod`|`object` (text)|The main method used to discover the planet (e.g., 'Transit', 'Radial Velocity').|

### Category 3: Core Features (X)

- **Project Use:** These are the _inputs_ we will feed into our model.
    
- **Model Use:** These are our **Features (X)**.
    

#### 3a. Planetary Features

|   |   |   |
|---|---|---|
|**Column Name**|**Datatype (in Pandas)**|**Easy Explanation**|
|`pl_orbper`|`float64` (number)|**Orbital Period:** How long the planet takes to circle its star (its "year").|
|`pl_orbsmax`|`float64` (number)|**Semi-Major Axis:** The average distance from the planet to its star.|
|`pl_rade`|`float64` (number)|**Planet Radius:** How big the planet is. Measured in multiples of Earth's radius.|
|`pl_masse`|`float64` (number)|**Planet Mass:** How heavy the planet is. Measured in multiples of Earth's mass.|
|`pl_dens`|`float64` (number)|**Density:** How "puffy" (like gas) or "compact" (like rock) the planet is.|
|`pl_orbeccen`|`float64` (number)|**Eccentricity:** How circular (`0`) or oval-shaped (`~1`) its orbit is.|
|`pl_eqt`|`float64` (number)|**Equilibrium Temperature:** A simple guess at the planet's average temperature.|
|`pl_insol`|`float64` (number)|**Insolation:** How much starlight/energy the planet gets from its star.|

#### 3b. Stellar Features

|   |   |   |
|---|---|---|
|**Column Name**|**Datatype (in Pandas)**|**Easy Explanation**|
|`st_teff`|`float64` (number)|**Star's Temperature:** How hot the star's surface is (in Kelvin).|
|`st_rad`|`float64` (number)|**Star's Radius:** How big the star is. Measured in multiples of our Sun's radius.|
|`st_mass`|`float64` (number)|**Star's Mass:** How heavy the star is. Measured in multiples of our Sun's mass.|
|`st_met`|`float64` (number)|**Star's Metallicity:** How rich the star is in "metals" (heavy elements).|
|`st_age`|`float64` (number)|**Star's Age:** The estimated age of the star in billions of years.|

#### 3c. System Features

|   |   |   |
|---|---|---|
|**Column Name**|**Datatype (in Pandas)**|**Easy Explanation**|
|`sy_snum`|`int64` (integer)|**Star Number:** How many stars are in the system (e.g., 1 for a single star, 2 for a binary).|
|`sy_pnum`|`int64` (integer)|**Planet Number:** How many known planets are in that star system.|
|`sy_dist`|`float64` (number)|**Distance:** How far away the system is from Earth.|
|`sy_vmag`|`float64` (number)|**V-Band Magnitude:** How bright the star _looks_ to us in visible light (lower number = brighter).|

### Category 4: Data Quality & Metadata (For Cleaning)

- **Project Use:** Use these to **clean and filter** our data _before_ training.
    
- **Model Use:** **DO NOT** use these as features.
    

|   |   |   |
|---|---|---|
|**Column Name**|**Datatype (in Pandas)**|**Easy Explanation**|
|`pl_orbpererr1`|`float64` (number)|The "plus" error bar for orbital period (e.g., 10 ± **0.1** days). A huge error means low quality.|
|`pl_orbpererr2`|`float64` (number)|The "minus" error bar for orbital period (e.g., 10 +0.1 / **-0.2** days).|
|`pl_radelim`|`int64` (integer)|**Limit Flag:** A `1` here means the radius isn't an exact measurement, just a _limit_ (e.g., "it's _less than_ this big").|
|`pl_controv_flag`|`int64` (integer)|**Controversy Flag:** A `1` means this planet's existence is debated. We should probably **remove** these rows.|
|`...err1`, `...err2`|`float64` (number)|_All_ columns ending in `err1` or `err2` are error values.|
|`...lim`|`int64` (integer)|_All_ columns ending in `lim` are limit flags.|
|`..._reflink`|`object` (text)|_All_ columns ending in `_reflink` are just citations for the data. We can ignore them.|

### Category 5: "Leakage" Columns (DO NOT USE AS FEATURES)

- **Project Use:** **CRITICAL:** We must **drop** these columns from our training data.
    
- **Model Use:** **DO NOT USE.** They "leak" the answer to the model, giving you a fake 100% score.
    

|   |   |   |
|---|---|---|
|**Column Name**|**Datatype (in Pandas)**|**Why to AVOID**|
|`disc_facility`|`object` (text)|The telescope/observatory that found it. This _directly_ tells you the method (e.g., 'Kepler Space Telescope' always means 'Transit').|
|`disc_telescope`|`object` (text)|Same as above. Leaks the answer.|
|`disc_instrument`|`object` (text)|The camera/instrument used. Leaks the answer (e.g., 'HARPS' always means 'Radial Velocity').|
|`rv_flag`|`int64` (integer)|A flag that is `1` if the planet was _ever_ observed with Radial Velocity. This is a dead giveaway.|
|`tran_flag`|`int64` (integer)|A flag that is `1` if the planet was _ever_ observed with Transit. Another dead giveaway.|
|`..._flag`|`int64` (integer)|_All_ other flags for detection methods (`pul_flag`, `ptv_flag`, `ast_flag`, etc.) must be dropped.|