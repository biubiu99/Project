library(shiny)
library(tidyverse)
ui <- fluidPage(
  
  dateInput('starting_date',
            label = 'Starting date in yyyy-mm-dd format',
            value = as.character("2021-02-01"),
            min = "2020-01-22", max = Sys.Date(),
            format = "yyyy-mm-dd",
            startview = 'year', language = 'en', weekstart = 1
  ),
  
  plotOutput(outputId = "time_series_plot" 
             
  ) 
)

server <- function(input, output){
  
  output$time_series_plot <- renderPlot({
    
    # You can use the R commands written from (2.1) to (2.6)
    data <- read.csv(url("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"))
    data
    data2.2 <-rename(data,Province = Province.State,Country=Country.Region)
    data2.3 <- data2.2 %>% filter(Country == "Canada")
    data2.4 <-data2.3%>% filter(Province !="Diamond Princess") %>% filter(Province !="Grand Princess") %>% filter(Province !="Repatriated Travellers")
    data2.5 <- data2.4 %>% gather(key = "date", value = "confirmed_cases", -Province, -Country, -Lat, -Long)  
    data2.5$date <- as.Date(data2.5$date,"X%m.%d.%y")
    confirmed_Canada <-data2.5
    
    
    # Let's say the data frame (tibble) 
    # you have by doing (2.1) - (2.6) is 
    # "confirmed_Canada". 
    # Now you can use the following to 
    # use the input date to select the rows: 
    confirmed_Canada <- filter(confirmed_Canada, date >= as.Date(as.character(input$starting_date)))
    
    # Use the R commands written for (2.7) to create the plot from confirmed_Canada data frame
    
    ggplot(confirmed_Canada,aes(date,confirmed_cases))+ geom_line(aes(color = Province))    
    
  }
  )
}

# Run the app
shinyApp(ui = ui, server = server)