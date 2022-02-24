class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon

    def epsilon_neighborhood(self, P):
        # TODO: implement next time
        return []


    def explore_and_assign_eps_neighborhood(self, P, cluster, assignments):
        # TODO: implement next time
        return assignments


    def dbscan(self):
        """
            returns a list of assignments. The index of the
            assignment should match the index of the data point
            in the dataset.
        """

        assignments = [0 for _ in range(len(self.dataset))]
        cluster = 1

        for P in range(len(self.dataset)):
            
            if assignments[P] != 0:
                # already part of a cluster
                continue

            if len(self.epsilon_neighborhood(P)) >= self.min_pts:
                # core point
                assignments = self.explore_and_assign_eps_neighborhood(
                    P, cluster, assignments)

            cluster += 1

        return assignments
