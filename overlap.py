# Overlap Graphs (Overlap-Layout-Consensus)

class Overlap:
    """
    Constructing the overlap graph.
    """
    def __init__(self, fasta):
        self.fasta = fasta
        self.dna = self.prepare_contigs()

    def prepare_contigs(self):
        res = []
        for contig in self.fasta:
            res.append([contig, contig])
            return res

    def overlap_graph(self, n):
        results = []
        for k1, v1 in self.dna:
            for k2, v2 in self.dna:
                if k1 != k2 and v1.endswith(v2[:n]):
                    results.append((k1, k2))

        return results