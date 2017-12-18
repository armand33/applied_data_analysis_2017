# Visualizing War
### *The Face of Geopolitics*

# Abstract

The fall of the berlin wall in 1989, meant the cold war was coming to an end and a New World Order was to be established. Using the data set provided by [UCDP](http://ucdp.uu.se/downloads/), we would like to tell the story of the geopolitics of the last \~thirty years by looking at the results of major crisis but also to countries that have undergone general instability in this period without real outburst of violence. The aim is to understand past political crises and provide tools to understand and predict the current and future political state of the world.

Our final data story is available [here](https://ucdp-world-conflicts.github.io).

Work done since milestone 2:
- Classification of actors has been done mainly by scraping wikipedia and matching the srcaping with actors from the data set. This is detailed in the [wikipedia_scraping](https://nbviewer.jupyter.org/github/armand33/applied_data_analysis_2017/blob/master/project/notebooks/wikipedia_scraping.ipynb?flush_cache=true) notebook.
- Data has been prepared for the visualizations (cleanning, matching, enrichment). This is detailed in the [milestone_3](https://nbviewer.jupyter.org/github/armand33/applied_data_analysis_2017/blob/master/project/notebooks/milestone_3.ipynb?flush_cache=true) notebook.
- Visualizations of the data have been build using [d3.js](https://d3js.org/) (three main scales of visualization (countries and regions and actors).
- The data story has been put together and is available [here](https://ucdp-world-conflicts.github.io).
_______________________________________________________
_______________________________________________________
# Milestone 2

The roadmap is the following:
- Start with some genral statistic about world safety (as in part 2)
- Detail some well known crisis such as the Rwandan genocide and compare them to some others (WWII, Shoah)
- Explore events in a groups (socialists uprisals, ethnic conflicts, cartel wars)
- Put those in relations with other data (economy, drought)

# Research questions
* How has the world evolved in terms of conflicts after the cold war, i.e., during the time span covered in the dataset?
* Which countries have undergone the most important crises during these time spans and which of those crises might be interlinked spatially and politically?
* Does the coverage of conflicts by media represent the real-world numbers in terms of number of conflicts and fatalities, or is there a bias?

# Dataset
We will use the UCDP data set that is available online as a csv file.

This data set lists events, that is incidents of lethal violence occuring at a given time and place between january 1989 and december 2013 (excluding Syria).  All those events are quantified, that means that it gives for each event the parties involved, the number of casualties on both side, the broader conflict if there is one, the time and place and the sources that reported the event.

For each event, we know exactly the longitude and latitude coordinates therefore we plot. So therefore, we can pinpoint the exact location of the event on a map.

Data can be filtered by type of violence (state-based, one-sided), general conflict, actor involved, location or date. For example, it is easy to retrieve data on the state conflicts in which the US has been involved in Africa since 1989. There is only one, against al-Quaida and it has led to the direct death of 97 persons, among which 68 members of al-Qaida and 12 civilians.

However, the data set does not contain anything about Syria. As it is currently a burning place in world affairs, it could be great to enrich the data set in order to include it.

# A list of internal milestones up until project milestone 2

- Data exploration : measure the full extent of the data set and the enventual gaps in it.
- Data cleaning : selected relevant data, fill the eventual gaps and format the data in a handful manner.
- Statistics responding to our first two question should be available by milestone 2.
- Define more precisely the angle in which we want to tell our data story depending on the findings of data exploration.

# Questions for TAs
- Is there any similar data set on Syria or covering 2013 to nowadays ?
- If yes can we enrich our data set using those ?
