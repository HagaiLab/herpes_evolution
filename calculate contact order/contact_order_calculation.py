# contact order function with df for example

csu_data = pd.read_csv("csu_df_for_example.csv", index_col=0)

def calc_contact_order(csu_df, min_seq_distance = 4, prefix=""):
    df = csu_df[csu_df["residual_dist"] >= min_seq_distance]

    amino_dist = (df.groupby(["target_protein"])
        .agg(sum_residual_dist=("residual_dist","sum"),
             count_residual_dist=("residual_dist","count"))
        .reset_index()
        )
    amino_dist.columns = ["target_protein", "sum_residual_dist", "count_residual_dist"]
    amino_dist[prefix + "abs_mean_contact_order"] = amino_dist["sum_residual_dist"] / amino_dist["count_residual_dist"]
    amino_dist.drop(["sum_residual_dist", "count_residual_dist"], axis=1)

    return amino_dist

display(calc_contact_order(protein_data_csu))


