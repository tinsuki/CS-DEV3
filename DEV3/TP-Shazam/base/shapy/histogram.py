# histograms are symmetric around 0, with a histogram_size = 2*histogram_width + 1

from settings import *
from hits import *

def histograms_new(width, songs):
  histograms = list()
  for s in range(songs):  # for each song
    histogram = list()
    for i in range(2*width+1):  # for each index
      histogram.append(0)
    histograms.append(histogram)
  return histograms

def histograms_accumulate(histograms, index, song):
  song = song - 1  # by convention, the song numbers start at 1 (not 0)
  histogram_size = len(histograms[0])
  histogram_width = int((histogram_size-1)/2)
  index = index + histogram_width  # 0 is at the center of the histogram indices
  if (0 <= index) and (index < histogram_size):
    histogram = histograms[song]
    histogram[index] = histogram[index] + 1
  else:
      print ("warning: index", index, "out of bounds")
  return histograms

def histograms_max(hits, counts, pair_count):
  # compute histograms
  histogram_width = hits_delta_range(hits)
  histograms = histograms_new(histogram_width, len(hits))
  for s in range(len(hits)):
    data = hits[s]
    for p in data:
      histograms_accumulate(histograms, p[1]-p[0], s+1)
  # then proceed...
  histogram_size = 2*histogram_width+1
  smax = 0  # prominent song
  imax = 0  # index of the global maximum
  vmax = 0  # corresponding value
  # for each song...
  for s in range(len(histograms)):
    histogram = histograms[s]
    # for each (delta) time index...
    limax = 0  # index of the local maximum (global for each song)
    lvmax = 0  # corresponding value
    for i in range(histogram_size):
      # get the (local) maximum
      if histogram[i] > lvmax:
        lvmax = histogram[i]  # (local) value
        limax = i  # (local) index
    # may update the global maximum
    if lvmax > vmax:
      vmax = lvmax  # maximum value
      imax = limax  # index
      smax = s+1  # song (by convention, song numbers start at 1)
    print ("song #%d got %d hits / %d" % (s+1, (histograms[s])[limax], counts[s+1]))
  # clear peak found?
  if not( (0 < imax) and (imax < histogram_width*2) ):  # out of bounds...
    return 0  # not found
  norm = min([counts[smax], pair_count])  #  smallest count used for histogram normalization
  if (histograms[smax-1])[imax] > (0.5 * norm):
    return smax;
  return 0  # not found...

# End Of File
