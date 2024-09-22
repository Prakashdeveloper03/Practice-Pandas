import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    return (
        actor_director.groupby(["actor_id", "director_id"])
        .size()
        .reset_index(name="cooperation_count")
        .query("cooperation_count >= 3")[["actor_id", "director_id"]]
    )
