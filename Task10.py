
cost_of_ride = 6
probability_of_being_caught = 0.05
probability_of_taxatoarea = 0.02
first_offense_cost = 50
second_offense_cost = 200
subsequent_offense_cost = 300
total_rides_per_year = 365 * 2

probability_of_no_cost = (1 - probability_of_taxatoarea) * (1 - probability_of_being_caught)

probability_of_paying_ride_cost = probability_of_taxatoarea

expected_cost_per_ride = (probability_of_no_cost * 0) + (probability_of_paying_ride_cost * cost_of_ride) + (probability_of_being_caught * first_offense_cost)

total_expected_cost = expected_cost_per_ride * total_rides_per_year

cost_for_students = cost_of_ride * total_rides_per_year

cost_difference = total_expected_cost - cost_for_students
print("Total expected cost", total_expected_cost, "\nCost for sutednts is", cost_for_students, "\nCost difference is", cost_difference)
