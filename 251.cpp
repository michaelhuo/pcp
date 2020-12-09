class Vector2D {
public:
    Vector2D(vector<vector<int>>& v) :outer(0), inner(0), data(v) {
        
    }
    
    int next() {
        advanceNext();
        int answer = data[outer][inner];
        inner += 1;
        if (inner == data[outer].size()) {
            outer += 1;
            inner = 0;
        }
        return answer;
    }
    
    bool hasNext() {
        advanceNext();
        return (outer < data.size());
    }
private:
    vector<vector<int>>& data;
    int outer;
    int inner;
    void advanceNext() {
        while (outer < data.size() && data[outer].empty()) {
            outer ++;
            inner = 0;
        }
    }
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D* obj = new Vector2D(v);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
