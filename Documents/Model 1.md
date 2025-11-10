Required Data-frame's Columns

| **Original Column Name** | **Your New (Suggested) Name** | **Purpose**                                               |
| ------------------------ | ----------------------------- | --------------------------------------------------------- |
| `pl_bmasse`              | `planet_mass_earth`           | **Group A:** To _create_ the `planet_type` target         |
| `pl_rade`                | `planet_radius_earth`         | **Group A:** To _create_ the `planet_type` target         |
| `pl_orbper`              | `planet_orb_period`           | **Group A** (for "Hot" rule) & **Group B** (as a feature) |
| `pl_orbsmax`             | `planet_orb_distance`         | **Group B:** Feature (X)                                  |
| `pl_orbeccen`            | `planet_orb_eccen`            | **Group B:** Feature (X)                                  |
| `st_teff`                | `star_temp`                   | **Group B:** Feature (X)                                  |
| `st_mass`                | `star_mass`                   | **Group B:** Feature (X)                                  |
| `st_met`                 | `star_metallicity`            | **Group B:** Feature (X)                                  |
| `sy_pnum`                | `system_planet_count`         | **Group B:** Feature (X)                                  |
| `pl_name`                | `planet_name`                 | **Group C:** Identifier                                   |
| `hostname`               | `star_name`                   | **Group C:** Identifier                                   |
