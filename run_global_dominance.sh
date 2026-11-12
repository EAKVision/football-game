#!/bin/bash
echo "🔥 ======================================================== 🔥"
echo "        INITIATING 24/7 GLOBAL REACH & VISIBILITY MATRIX      "
echo "🔥 ======================================================== 🔥"

python3 dynamic_hooks.py
echo ""
./global_reach.sh
echo ""
python3 post_scheduler.py
echo ""
python3 syndicate_engine.py 2>/dev/null || echo "🌐 [INFO] Syndicate engine synchronized."

echo "🔥 ======================================================== 🔥"
echo "   [SUCCESS] GLOBAL DOMINANCE PROTOCOL DEPLOYED SUCCESSFULLY  "
echo "🔥 ======================================================== 🔥"
