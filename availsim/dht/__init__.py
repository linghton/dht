import chord, dhash, oracle, totalrecall

# For automatic use by availsim
known_types = {
    'chord': chord,
    'dhash': dhash.dhash,
    'fragments': dhash.dhash_fragments,
    'replica': dhash.dhash_replica,
    'cates': dhash.dhash_cates,
    'replica_durability_oracle': oracle.durability_oracle,
    'replica_availability_oracle': oracle.availability_oracle,
    'total_recall_replica': totalrecall.totalrecall_lazy_replica
}
