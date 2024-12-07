#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <filesystem>  
#include <unistd.h>  

using namespace std;

struct FormatResult {
    vector<long long> testValues;
    vector<vector<long long>> combine;
};

vector<string> readFile(const string& filename) {
    vector<string> lines;
    string currentPath = filesystem::current_path().string();
    string fullPath = currentPath + "/" + filename;
    ifstream file(fullPath);
    
    if (!file.is_open()) {
        return lines;
    }
    
    string line;
    while (getline(file, line)) {
        lines.push_back(line);
    }
    return lines;
}

FormatResult format(const vector<string>& lines) {
    FormatResult result;
    
    for (const string& line : lines) {
        size_t pos = line.find(':');
        string val = line.substr(0, pos);
        string row = line.substr(pos + 1);
        
        result.testValues.push_back(stoll(val));
        
        stringstream ss(row);
        vector<long long> nums;
        string num;
        while (ss >> num) {
            nums.push_back(stoll(num));
        }
        result.combine.push_back(nums);
    }
    return result;
}

void generateCombinations(vector<vector<string>>& result, vector<string>& current, 
                        int ops, const vector<string>& items) {
    if (current.size() == ops) {
        result.push_back(current);
        return;
    }
    for (const string& item : items) {
        current.push_back(item);
        generateCombinations(result, current, ops, items);
        current.pop_back();
    }
}

vector<vector<string>> generateOperators(int ops, bool part2) {
    vector<string> items = {"*", "+"};
    if (part2) items.push_back("||");
    
    vector<vector<string>> result;
    vector<string> current;
    generateCombinations(result, current, ops, items);
    return result;
}

long long partOne(const string& file) {
    vector<string> lines = readFile(file);
    FormatResult formatted = format(lines);
    long long result = 0;
    
    for (size_t i = 0; i < formatted.testValues.size(); i++) {
        const vector<long long>& nums = formatted.combine[i];
        long long testV = formatted.testValues[i];
        vector<vector<string>> ops = generateOperators(nums.size() - 1, false);
        
        for (const auto& combination : ops) {
            long long curr = nums[0];
            size_t idx = 1;
            
            for (const string& op : combination) {
                if (op == "+") {
                    curr += nums[idx];
                } else if (op == "*") {
                    curr *= nums[idx];
                }
                idx++;
            }
            
            if (curr == testV) {
                result += testV;
                break;
            }
        }
    }
    return result;
}

long long partTwo(const string& file) {
    vector<string> lines = readFile(file);
    FormatResult formatted = format(lines);
    long long result = 0;
    
    for (size_t i = 0; i < formatted.testValues.size(); i++) {
        const vector<long long>& nums = formatted.combine[i];
        long long testV = formatted.testValues[i];
        vector<vector<string>> ops = generateOperators(nums.size() - 1, true);
        
        for (const auto& combination : ops) {
            long long curr = nums[0];
            size_t idx = 1;
            
            for (const string& op : combination) {
                if (op == "+") {
                    curr += nums[idx];
                } else if (op == "*") {
                    curr *= nums[idx];
                } else if (op == "||") {
                    // Replace string concatenation with numeric approach
                    long long temp = nums[idx];
                    long long multiplier = 1;
                    while (temp > 0) {
                        temp /= 10;
                        multiplier *= 10;
                    }
                    curr = curr * multiplier + nums[idx];
                }
                idx++;
            }
            
            if (curr == testV) {
                result += testV;
                break;
            }
        }
    }
    return result;
}

int main() {
   auto start1 = chrono::high_resolution_clock::now();
    long long one = partOne("data.txt");
    auto end1 = chrono::high_resolution_clock::now();
    auto duration1 = chrono::duration_cast<chrono::milliseconds>(end1 - start1);
    
    // Start timer for Part 2
    auto start2 = chrono::high_resolution_clock::now();
    long long two = partTwo("data.txt");
    auto end2 = chrono::high_resolution_clock::now();
    auto duration2 = chrono::duration_cast<chrono::milliseconds>(end2 - start2);
    
    cout << "Part 1: " << one << " (Time: " << duration1.count() << "ms)" << endl;
    cout << "Part 2: " << two << " (Time: " << duration2.count() << "ms)" << endl;
    
    // Total time
    cout << "Total Time: " << (duration1 + duration2).count() << "ms" << endl;
    
    return 0;
}