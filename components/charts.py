import plotly.express as px


def trust_chart(df):

    fig = px.bar(
        df,
        x="worker_id",
        y="trust_score",
        title="Worker Trust Intelligence"
    )

    fig.update_layout(
        height=350
    )

    return fig



def skill_chart(df):

    fig = px.scatter(
        df,
        x="experience_years",
        y="reliability_score",
        size="trust_score",
        color="community_id",
        title="Human Capital Map"
    )

    return fig